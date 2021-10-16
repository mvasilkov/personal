#!/usr/bin/env python3

from pbuild.external import git, pandoc, sass
from pbuild.pages import build_pages


def run():
    git.check_available()
    pandoc.check_available()
    sass.check_available()

    build_pages()


if __name__ == '__main__':
    run()
