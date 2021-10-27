#!/usr/bin/env python3

from pbuild.external import git, pandoc, sass, lessc, cleancss
from pbuild.pages import build_pages
from pbuild.stylesheets import build_css


def run():
    git.git_check_available()
    pandoc.pandoc_check_available()
    sass.sass_check_available()
    lessc.lessc_check_available()
    cleancss.cleancss_check_available()

    build_pages()
    build_css()


if __name__ == '__main__':
    run()
