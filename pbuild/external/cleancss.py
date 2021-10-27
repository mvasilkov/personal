import re
from subprocess import check_output

from pbuild.settings import NODE_MODULES, NODE_USE_SHELL

CLEANCSS_EXECUTABLE = NODE_MODULES / '.bin' / 'cleancss'


def cleancss_check_available():
    try:
        result = check_output([CLEANCSS_EXECUTABLE, '--version'], encoding='utf-8', shell=NODE_USE_SHELL)
    except FileNotFoundError:
        raise RuntimeError('Cannot run cleancss')

    version = re.match(r'(.+?)$', result, re.MULTILINE)
    if version is None:
        raise RuntimeError(f'Cannot understand cleancss, got {result!r}')

    version_tuple = tuple(version.group(1).split('.'))
    if version_tuple[0] != '5':
        raise RuntimeError(f'Expected cleancss version 5, got {version.group(1)!r}')

    return version_tuple
