import re
from subprocess import check_call, check_output


def check_available():
    try:
        result = check_output(['git', '--version'], encoding='utf-8')
    except FileNotFoundError:
        raise RuntimeError('Cannot run git')

    version = re.match(r'git version (.+?)$', result, re.MULTILINE)
    if version is None:
        raise RuntimeError(f'Cannot understand git, got {result!r}')

    version_tuple = tuple(version.group(1).split('.'))
    if version_tuple[0] != '2':
        raise RuntimeError(f'Expected git 2, got {version.group(1)!r}')

    return version_tuple


def git_clean_out():
    try:
        check_call(['git', 'clean', '--force', '--quiet', '-x', 'out'])
    except FileNotFoundError:
        raise RuntimeError('Cannot run git clean')
