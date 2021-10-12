from django.template import Context, Engine

from build.settings import PHP_ROOT

TEMPLATES_DIR = PHP_ROOT / 'templates'


def render_to_file(template_name: str, context_dict: dict, out_file):
    engine = Engine(dirs=[TEMPLATES_DIR.as_posix()])
    template = engine.get_template(template_name)
    result = template.render(Context(context_dict))
