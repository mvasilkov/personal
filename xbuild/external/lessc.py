import re
from subprocess import check_output

from xbuild.settings import NODE_MODULES, NODE_USE_SHELL

LESSC_EXECUTABLE = NODE_MODULES / '.bin' / 'lessc'


def lessc_check_available():
    try:
        result = check_output([LESSC_EXECUTABLE, '--version'], encoding='utf-8', shell=NODE_USE_SHELL)
    except FileNotFoundError:
        raise RuntimeError('Cannot run lessc')

    version = re.match(r'lessc (.+?)$', result, re.MULTILINE)
    if version is None:
        raise RuntimeError(f'Cannot understand lessc, got {result!r}')

    version_tuple = tuple(version.group(1).split('.'))
    if version_tuple[0] != '4':
        raise RuntimeError(f'Expected lessc version 4, got {version.group(1)!r}')

    return version_tuple


def lessc_get_stylesheet(path):
    try:
        result = check_output([LESSC_EXECUTABLE, path], encoding='utf-8', shell=NODE_USE_SHELL)
    except FileNotFoundError:
        raise RuntimeError(f'Cannot run lessc {path!r}')

    return result
