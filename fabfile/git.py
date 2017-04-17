#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module hold fabric management functions dealing with Git
'''

# Imports #####################################################################
from fabric.api import task
from fabric.utils import abort
from .helpers import ex, user_input, true
from .ver import get_version


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


def get_tags():
    '''Returns a list of tags'''
    (text, _) = ex(['git', 'tag', '-l', '--sort=version:refname', '"*"'])

    if text:
        return text.split('\n')

    return []


@task
def tag():
    '''Create a tag'''
    current_version = get_version()
    tags = get_tags()

    print("...current version is: %s" % current_version)
    if tags:
        print("...latest tag is: %s" % tags[-1])

    name = user_input("Enter tag to create: ")
    name = "v" + name if not name.startswith('v') else name
    message = "creating tag %s" % name

    answer = user_input("creating tag [%s].  OK? " % name)
    if not true(answer):
        abort("Aborting tag creation")

    ex(['git', 'tag', '-a', name, '-m', '"%s"' % message])
    ex(['git', 'push', 'origin', '--tags'])
