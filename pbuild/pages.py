from ast import literal_eval
from dataclasses import asdict, dataclass
from typing import Generator, cast

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

from pbuild.external.git import git_clean_out, git_log_created, git_log_updated
from pbuild.external.pandoc import pandoc_get_page
from pbuild.settings import PHP_ROOT
from pbuild.templates import render_to_file

PAGES_DIR = PHP_ROOT / 'pages'
OUT_DIR = PHP_ROOT / 'out'


@dataclass
class PageProps:
    title: str = ''
    content: str = ''
    created: int = 0
    updated: int = 0
    use_katex: bool = False


def build_pages():
    pages = list(PAGES_DIR.rglob('*.md'))

    # Clean
    git_clean_out()

    # Make dirs
    dirs_rel = {p.parent.relative_to(PAGES_DIR) for p in pages}
    for r in dirs_rel:
        out_dir = OUT_DIR / r

        if out_dir.exists():
            if not out_dir.is_dir():
                raise RuntimeError(f'Should be a directory: {out_dir}')
            continue

        out_dir.mkdir(parents=True)

    # Build pages
    for page_path in pages:
        page_content = pandoc_get_page(page_path)
        props = get_page_props(page_content)
        props.created = git_log_created(page_path)
        props.updated = git_log_updated(page_path)

        out_file = OUT_DIR / page_path.relative_to(PAGES_DIR).with_suffix('.html')
        print('Writing', out_file)
        render_to_file('page.html', asdict(props), out_file)


def get_page_props(page_content: str) -> PageProps:
    soup = BeautifulSoup(page_content, 'html5lib', multi_valued_attributes=None)
    if soup.body is None:
        raise RuntimeError('BeautifulSoup broke')

    use_katex = soup.find(class_='math display') is not None

    children = cast(
        Generator[Tag, None, None],
        (a for a in soup.body.children if type(a) is not NavigableString),
    )
    first_child = next(children)
    second_child = next(children)

    if first_child.name == 'h1':
        return PageProps(title=first_child.get_text(), content=page_content, use_katex=use_katex)

    if first_child.name == 'pre' and first_child.get('class') == 'python':
        options = literal_eval(first_child.get_text())
        options['content'] = clean_options(page_content)
        options['use_katex'] = use_katex
        props = PageProps(**options)

        if not props.title:
            if second_child.name != 'h1':
                raise RuntimeError('Missing title')

            props.title = second_child.get_text()

        return props

    raise RuntimeError('Missing title and options')


def clean_options(page_content: str) -> str:
    return page_content.split('</code></pre>\n', 1).pop()
