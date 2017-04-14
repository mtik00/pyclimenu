#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module holds the function for building the python installers.
'''

# Imports #####################################################################
import os
import sys
from fabric.api import task
from fabric.colors import green

from .helpers import ex, remove_directory
from .constants import LIB_DIR


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-APR-2017'


# Globals #####################################################################
def _build():
    pass


@task
def build():
    '''Build the release'''
    dist_dir = os.path.join(LIB_DIR, 'dist')
    setup_path = os.path.join(LIB_DIR, 'setup.py')
    command = [
        sys.executable,
        setup_path,
        'build',
        'sdist',
        '--formats',
        'gztar',
        'bdist_wheel'
    ]

    # Delete older releases
    remove_directory(dist_dir, remove_top=False)

    ex(command)

    # Remove the egg-info directory
    egg_info = next((
        x for x in os.listdir(LIB_DIR) if (x == 'climenu.egg-info')), None)

    if egg_info:
        egg_info = os.path.join(LIB_DIR, egg_info)
        remove_directory(egg_info)

    builds = ', '.join(os.listdir(dist_dir))
    print(green("built: %s" % builds))
