#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module hold fabric management functions dealing with Git
'''

# Imports #####################################################################
from collections import namedtuple
from pkg_resources import parse_version

from fabric.api import task
from fabric.utils import abort
from .helpers import ex, user_input, true
from .ver import get_version


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-APR-2017'


# Globals #####################################################################

VERSIONED_TAG = namedtuple('VersionedTag', 'string version')


def on_master():
    '''Returns True if we're currently on the master branch'''
    (text, _) = ex(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    return "master" in text.lower()


def is_clean():
    '''Returns True if nothing is staged or untracked'''
    (text, _) = ex(['git', 'status', '--porcelain'])
    return (not bool(text), text)


@task
def get_tags():
    '''Returns a list of tags'''
    result = []
    (text, _) = ex('git tag -l --sort=version:refname "*"')

    for line in text.splitlines():
        result.append(VERSIONED_TAG(line, parse_version(line)))

    return sorted(result, cmp=lambda x, y: cmp(x.version, y.version))


@task
def tag():
    '''Create a tag'''
    current_version = get_version()
    tags = get_tags()
    latest_tag = tags[-1] if tags else ''

    print("...current version is: v%s" % current_version)
    if latest_tag:
        print("...latest tag is: %s" % latest_tag.string)

    default_version = 'v%s' % current_version

    name = user_input("Enter tag to create [default to: %s]: " % default_version)

    name = name or default_version
    name = "v" + name if not name.startswith('v') else name
    message = "creating tag %s" % name

    answer = user_input("creating tag [%s].  OK? " % name)
    if not true(answer):
        abort("Aborting tag creation")

    ex(['git', 'tag', '-a', name, '-m', '"%s"' % message])
    ex(['git', 'push', 'origin', '--tags'])
