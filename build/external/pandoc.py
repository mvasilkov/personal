import re
from subprocess import check_output


def check_available():
    try:
        result = check_output(['pandoc', '--version'], encoding='utf-8')
    except FileNotFoundError:
        raise RuntimeError('Cannot run pandoc')

    version = re.match(r'pandoc (.+?)$', result, re.MULTILINE)
    if version is None:
        raise RuntimeError(f'Cannot understand pandoc, got {result!r}')

    version_tuple = tuple(version.group(1).split('.'))
    if version_tuple[0] != '2':
        raise RuntimeError(f'Expected pandoc 2, got {version.group(1)!r}')

    return version_tuple
