#!/usr/bin/env python3

from pebuild.external import git, pandoc
from pebuild.pages import build_pages


def run():
    git.check_available()
    pandoc.check_available()

    build_pages()


if __name__ == '__main__':
    run()
