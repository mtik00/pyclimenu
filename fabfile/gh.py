#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module holds function dealing with GitHub.
'''

# Imports #####################################################################
from __future__ import print_function
import os
import github
from fabric.api import task
from fabric.utils import abort

from .constants import LIB_DIR, DIST_DIR
from .helpers import ex, abspath
from .git import get_tags
from .relnote import get as get_release_notes


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-APR-2017'


# Globals #####################################################################
GITHUB_USER = os.environ['GH_USERNAME']
GITHUB_TOKEN = os.environ['GH_TOKEN']
REPO_NAME = 'pyclimenu'


def repo():
    '''Retrieve the GitHub repo'''
    g = github.Github(GITHUB_USER, GITHUB_TOKEN)
    u = g.get_user()
    r = u.get_repo(REPO_NAME)
    return r


def repo_list():
    '''Retrieves a list of repos'''
    g = github.Github(GITHUB_USER, GITHUB_TOKEN)
    u = g.get_user()
    print([x.name for x in u.get_repos()])


@task
def create_release(tag=None, message=None):
    '''Create a GitHub release'''
    if not tag:
        tag = get_tags()[-1].string

    if not message:
        message = get_release_notes(tag)

    r = repo()
    r.create_git_release(tag, tag, message)


def _upload():
    tag = get_tags()[-1]

    # Make sure the release exists
    r = repo()
    github_release = next((
        x for x in r.get_releases() if x.tag_name == tag.string),
        None)

    if not github_release:
        create_release(tag.string)

    # Find the tarball
    path = None
    for fname in os.listdir(DIST_DIR):
        if (str(tag.version) in fname) and fname.endswith('.tar.gz'):
            path = abspath(DIST_DIR, fname)
            break

    if not path:
        abort("Could not find tarball matching %s" % str(tag.version))

    # Make life easier and call ``github-release.exe``
    upload_bin = os.path.join(LIB_DIR, 'bin', 'github-release.exe')

    if not os.path.exists(upload_bin):
        raise Exception("github-release.exe not found")

    cmd = [
        upload_bin, 'upload', '-s', GITHUB_TOKEN, '-u', 'mtik00',
        '-r', REPO_NAME, '-t', tag.string, '-n', os.path.basename(path), '-f', path
    ]

    ex(cmd)


@task
def upload():
    '''Attaches a file to a tag'''
    _upload()
