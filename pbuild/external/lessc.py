import platform
import re
from subprocess import check_output

from pbuild.settings import NODE_MODULES

LESSC_EXECUTABLE = NODE_MODULES / '.bin' / 'lessc'
USE_SHELL = platform.system() == 'Windows'


def check_available():
    try:
        result = check_output([LESSC_EXECUTABLE, '--version'], encoding='utf-8', shell=USE_SHELL)
    except FileNotFoundError:
        raise RuntimeError('Cannot run lessc')

    version = re.match(r'lessc (.+?)$', result, re.MULTILINE)
    if version is None:
        raise RuntimeError(f'Cannot understand lessc, got {result!r}')

    version_tuple = tuple(version.group(1).split('.'))
    if version_tuple[0] != '4':
        raise RuntimeError(f'Expected lessc version 4, got {version.group(1)!r}')

    return version_tuple
