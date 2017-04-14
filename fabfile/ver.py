#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module manages the version info.
'''

# Imports #####################################################################
import re
# from fabric.api import task
from .constants import VER_FILE


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
