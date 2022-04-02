from functools import cache
from pathlib import Path

from django.template import Context, Engine

from xbuild.settings import PHP_ROOT

TEMPLATES_DIR = PHP_ROOT / 'templates'


@cache
def get_engine():
    return Engine(dirs=[TEMPLATES_DIR.as_posix()])


@cache
def get_template(template_name: str):
    return get_engine().get_template(template_name)


def render_to_file(template_name: str, context_dict: dict, out_file: Path):
    template = get_template(template_name)
    result = template.render(Context(context_dict))

    with open(out_file, 'w', encoding='utf-8', newline='\n') as out:
        out.write(result)
