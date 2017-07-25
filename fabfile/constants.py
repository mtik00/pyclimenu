#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module holds the common constants used across Fabric.
'''

# Imports #####################################################################
import os

# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '13-APR-2017'


# Globals #####################################################################
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
LIB_DIR = os.path.join(THIS_DIR, '..')
VER_FILE = os.path.join(LIB_DIR, 'climenu.py')
DIST_DIR = os.path.join(LIB_DIR, 'dist')
RELEASE_NOTES_FILE = os.path.join(LIB_DIR, 'release-notes.md')
DOCS_CONF_FILE = os.path.join(LIB_DIR, 'docs', 'conf.py')
