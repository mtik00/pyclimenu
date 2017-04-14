#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module holds the management functions for interacting wity Pypi
'''

# Imports #####################################################################
from .helpers import ex


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-APR-2017'


# Globals #####################################################################
def upload():
    '''Upload the release files to Pypi'''
    command = 'dir'  # ['twine', 'upload', 'dist/*']
    ex(command)
