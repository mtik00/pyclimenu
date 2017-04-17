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

from .constants import LIB_DIR
from .helpers import ex


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


@task
def repo_list():
    '''Retrieves a list of repos'''
    g = github.Github(GITHUB_USER, GITHUB_TOKEN)
    u = g.get_user()
    print([x.name for x in u.get_repos()])


def create_release(tag, message=None):
    '''Create a GitHub release'''
    message = message or '%s release' % tag

    r = repo()
    r.create_git_release(tag, tag, message)


@task
def upload(tag, path):
    '''Attaches a file to a tag'''
    # Make sure the release exists
    r = repo()

    github_release = next((
        x for x in r.get_releases() if x.tag_name == tag),
        None)

    if not github_release:
        abort("GitHub release for [%s] not found" % tag)

    # Make life easier and call ``github-release.exe``
    upload_bin = os.path.join(LIB_DIR, 'bin', 'github-release.exe')

    if not os.path.exists(upload_bin):
        raise Exception("github-release.exe not found")

    cmd = [
        upload_bin, 'upload', '-s', GITHUB_TOKEN, '-u', 'mtik00',
        '-r', REPO_NAME, '-t', tag, '-n', os.path.basename(path), '-f', path
    ]

    ex(cmd)
