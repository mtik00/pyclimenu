#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module manages the version info.
'''

# Imports #####################################################################
import re
from fabric.api import task
from .constants import VER_FILE, DOCS_CONF_FILE
from .helpers import true


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '13-APR-2017'


# Globals #####################################################################
RE_VERSION = re.compile(
    '^__version__\s*=\s*[\'"](?P<version>.*?)[\'"]\s*?^', re.MULTILINE)


def get_version():
    '''Gets the current version'''
    text = open(VER_FILE).read()
    match = RE_VERSION.search(text)

    if not match:
        raise Exception("Could not get version")

    return match.group('version')


@task
def rev():
    """Increases the 'minor' version number by 1"""
    text = open(VER_FILE).read()
    whole, ver = re.search("^(__version__\s+=\s+['\"](.*?)['\"]\s*)$", text, re.MULTILINE).groups()
    major, minor, patch = ver.split('.', 2)
    new_minor = str(int(minor) + 1)

    # NOTE: When reving minor, it's customary to set patch to "0"
    new_ver = ".".join([major, new_minor, "0"])

    print("Old version number is [%s]" % ver)
    print("New version number is [%s]" % new_ver)
    val = raw_input("OK [Yn]? ")
    while not true(val):
        new_ver = raw_input("Enter new version: ")
        print("Using new version [%s]" % new_ver)
        val = raw_input("OK [Yn]? ")

    text = text.replace(ver, new_ver)
    with open(VER_FILE, "wb") as fh:
        fh.write(text)

    text = open(DOCS_CONF_FILE).read()
    text = re.sub("(version|release) = u'.*?'", r"\1 = u'%s'" % new_ver, text)
    with open(DOCS_CONF_FILE, 'wb') as fh:
        fh.write(text)
