import re
from subprocess import check_output

from pebuild.settings import PHP_ROOT

SASS_EXECUTABLE = PHP_ROOT / 'node_modules' / '.bin' / 'sass'


def check_available():
    try:
        result = check_output([SASS_EXECUTABLE, '--version'], encoding='utf-8', shell=True)
    except FileNotFoundError:
        raise RuntimeError('Cannot run sass')

    version = re.match(r'(.+?)$', result, re.MULTILINE)
    if version is None:
        raise RuntimeError(f'Cannot understand sass, got {result!r}')

    version_tuple = tuple(version.group(1).split('.'))
    if version_tuple[0] != '1':
        raise RuntimeError(f'Expected sass version 1, got {version.group(1)!r}')

    return version_tuple
