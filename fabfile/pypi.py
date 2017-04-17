#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module holds the management functions for interacting wity Pypi
'''

# Imports #####################################################################
from .helpers import ex
from fabric.api import task


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-APR-2017'


# Globals #####################################################################
@task
def upload():
    '''Upload the release files to Pypi'''
    command = ['twine', 'upload', 'dist/*']
    ex(command)
