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

from .ver import get_version
from .helpers import ex, true

if sys.version_info.major > 2:
    raw_input = input


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '13-APR-2017'


# Globals #####################################################################
@task
def release(clean='y'):
    '''Build and release

    :param bool clean: Check to make sure the workspace is clean
    '''
    # Make sure we're on the master branch
    (text, _) = ex(['git', 'status'])
    if "On branch master" not in text:
        abort(("Only releasing from branch `master` is supported"))

    # Make sure there's everything's checked in
    if true(clean):
        (text, _) = ex(['git', 'status', '--porcelain'])
        if text:
            abort("Staging area is not clean:\n%s" % red(text))

    ver = get_version()
    print("Releasing v%s" % ver)
    val = raw_input("...OK? ")
    if not true(val):
        abort("User aborted")
