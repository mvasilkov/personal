from build.settings import PHP_ROOT

PAGES_DIR = PHP_ROOT / 'pages'
OUT_DIR = PHP_ROOT / 'out'


def build_pages():
    pages = PAGES_DIR.rglob('*.md')

    # Make dirs
    dirs_rel = {p.parent.relative_to(PAGES_DIR) for p in pages}
    for r in dirs_rel:
        out_dir = OUT_DIR / r

        if out_dir.exists():
            if not out_dir.is_dir():
                raise RuntimeError(f'Should be a directory: {out_dir}')
            continue

        out_dir.mkdir(parents=True)
