from xbuild.external.lessc import lessc_get_stylesheet
from xbuild.external.sass import sass_get_stylesheet
from xbuild.external.cleancss import cleancss_optimize
from xbuild.settings import OUR_ROOT


def build_css():
    css = sass_get_stylesheet(OUR_ROOT / 'stylesheets' / 'app.scss')
    out_file = OUR_ROOT / 'out' / 'static' / 'app.css'

    print('Writing', out_file)

    with open(out_file, 'w', encoding='utf-8', newline='\n') as out:
        out.write(css)

    cleancss_optimize(out_file)

    css = lessc_get_stylesheet(OUR_ROOT / 'stylesheets' / 'katex.less')
    out_file = OUR_ROOT / 'out' / 'static' / 'katex.css'

    print('Writing', out_file)

    with open(out_file, 'w', encoding='utf-8', newline='\n') as out:
        out.write(css)

    cleancss_optimize(out_file)
