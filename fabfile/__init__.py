#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module is used to manage the pyclimenu project.
'''

# Imports #####################################################################
from __future__ import print_function
import sys
from fabric.api import task
from fabric.utils import abort
from fabric.colors import red

from .git import on_master, is_clean
from .ver import get_version
from .helpers import true
from .build import build
from .pypi import upload
from .gh import repo_list


if sys.version_info.major > 2:
    raw_input = input


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '13-APR-2017'


# Globals #####################################################################
@task
def release(clean='y', pypi='y'):
    '''Build and release

    :param bool clean: Check to make sure the workspace is clean
    '''
    print(repo_list())

    if not on_master():
        abort(("Only releasing from branch `master` is supported"))

    # Make sure there's everything's checked in
    if true(clean):
        clean, text = is_clean()
        if not clean:
            abort("Staging area is not clean:\n%s" % red(text))

    ver = get_version()
    print("Releasing v%s" % ver)
    val = raw_input("...OK? ")
    if not true(val):
        abort("User aborted")

    # Build the release
    build()

    # Upload to pypi
    if true(pypi):
        upload()
