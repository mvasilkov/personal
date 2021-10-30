from pathlib import Path
import re
from subprocess import check_call, check_output

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


def cleancss_optimize(in_path: Path, out_path: Path = None, delete=True):
    if out_path is None:
        out_path = in_path.with_stem(f'{in_path.stem}-min')

    try:
        check_call(
            [
                CLEANCSS_EXECUTABLE,
                '-O1',
                'specialComments:0',
                '--output',
                out_path,
                '--',
                in_path,
            ],
            shell=NODE_USE_SHELL,
        )
    except FileNotFoundError:
        raise RuntimeError(f'Cannot run cleancss {in_path!r}')

    if delete:
        in_path.unlink()
