#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module hold fabric management functions dealing with Git
'''

# Imports #####################################################################
from .helpers import ex


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-APR-2017'


# Globals #####################################################################
def on_master():
    '''Returns True if we're currently on the master branch'''
    (text, _) = ex(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    return "master" in text.lower()


def is_clean():
    '''Returns True if nothing is staged or untracked'''
    (text, _) = ex(['git', 'status', '--porcelain'])
    return (not bool(text), text)
