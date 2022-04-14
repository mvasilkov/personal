#!/usr/bin/env python3

import django
from django.conf import settings

from xbuild.external import git, pandoc, sass, lessc, cleancss
from xbuild.pages import build_pages
from xbuild.stylesheets import build_css


def run():
    git.git_check_available()
    pandoc.pandoc_check_available()
    sass.sass_check_available()
    lessc.lessc_check_available()
    cleancss.cleancss_check_available()

    settings.configure()
    django.setup()

    build_pages()
    build_css()


if __name__ == '__main__':
    run()
