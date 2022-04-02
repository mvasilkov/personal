from xbuild.external.lessc import lessc_get_stylesheet
from xbuild.external.sass import sass_get_stylesheet
from xbuild.external.cleancss import cleancss_optimize
from xbuild.settings import PHP_ROOT


def build_css():
    css = sass_get_stylesheet(PHP_ROOT / 'stylesheets' / 'app.scss')
    out_file = PHP_ROOT / 'out' / 'static' / 'app.css'

    print('Writing', out_file)

    with open(out_file, 'w', encoding='utf-8', newline='\n') as out:
        out.write(css)

    cleancss_optimize(out_file)

    css = lessc_get_stylesheet(PHP_ROOT / 'stylesheets' / 'katex.less')
    out_file = PHP_ROOT / 'out' / 'static' / 'katex.css'

    print('Writing', out_file)

    with open(out_file, 'w', encoding='utf-8', newline='\n') as out:
        out.write(css)

    cleancss_optimize(out_file)
