#!/usr/bin/env python3

from pbuild.external import git, pandoc, sass
from pbuild.pages import build_pages
from pbuild.stylesheets import build_css


def run():
    git.check_available()
    pandoc.check_available()
    sass.check_available()

    build_pages()
    build_css()


if __name__ == '__main__':
    run()
