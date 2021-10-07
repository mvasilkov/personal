from ast import literal_eval
from dataclasses import dataclass

from bs4 import BeautifulSoup, NavigableString

from build.external.git import git_clean_out
from build.external.pandoc import pandoc_get_page
from build.settings import PHP_ROOT

PAGES_DIR = PHP_ROOT / 'pages'
OUT_DIR = PHP_ROOT / 'out'


@dataclass
class PageProps:
    title: str = ''
    created: int = 0
    updated: int = 0


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

        print(page_content)

        props = get_page_props(page_content)

        print(props)


def get_page_props(page_content: str):
    soup = BeautifulSoup(page_content, 'html5lib', multi_valued_attributes=None)
    assert soup.body is not None

    children = (a for a in soup.body.children if type(a) is not NavigableString)
    first_child = next(children)
    second_child = next(children)

    if first_child.name == 'h1':
        return PageProps(title=first_child.get_text())

    if first_child.name == 'pre' and first_child.get('class') == 'python':
        options = literal_eval(first_child.get_text())
        props = PageProps(**options)

        if not props.title:
            assert second_child.name == 'h1'

            props.title = second_child.get_text()

        return props

    assert False
