from pbuild.external.sass import sass_get_stylesheet
from pbuild.settings import PHP_ROOT


def build_css():
    css = sass_get_stylesheet(PHP_ROOT / 'stylesheets' / 'app.scss')
    out_file = PHP_ROOT / 'out' / 'static' / 'app.css'

    with open(out_file, 'w', encoding='utf-8', newline='\n') as out:
        out.write(css)
