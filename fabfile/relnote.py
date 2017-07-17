#!/usr/bin/env python2.7
# coding: utf-8
"""
This script is used for project management.

See Fabric documentation for more info: http://docs.fabfile.org/en/1.10/index.html
"""

# Imports #####################################################################
from __future__ import print_function
import os
import re
from markdown import markdown
from fabric.api import env, task
from fabric.colors import red

# Internal
from .helpers import true, ex
from .constants import RELEASE_NOTES_FILE
from .ver import get_version

# Metadata ####################################################################
__author__ = "Timothy McFadden"
__creationDate__ = "07-JUL-2017"


# Fabric environment setup ####################################################
env.colorize_errors = True
###############################################################################


def _get(version=None, path=RELEASE_NOTES_FILE, html='n', display='n'):
    '''Return only the release notes for the specified version'''
    version = version or get_version()
    text = open(path).read()

    match = re.search('^(?P<notes># v?{0}.*?)^\*+$\n^$'.format(version), text, re.MULTILINE | re.DOTALL)
    if match:
        notes = match.group('notes').strip()
        if true(html):
            notes = markdown(notes, extensions=['markdown.extensions.fenced_code'])

        if true(display):
            print(notes)

        return notes

    print("WARNING: No release notes found for [%s]" % version)


@task
def get(version=None, path=RELEASE_NOTES_FILE, html='n', display='y'):
    '''Return only the release notes for the specified version'''
    return _get(version, path, html, display)
