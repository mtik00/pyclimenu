#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module holds function dealing with GitHub.
'''

# Imports #####################################################################
import os
import github
from fabric.api import task


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-APR-2017'


# Globals #####################################################################
GITHUB_USER = os.environ['GH_USERNAME']
GITHUB_TOKEN = os.environ['GH_TOKEN']
REPO_NAME = 'pyclimenu'


@task
def repo():
    '''Retrieve the GitHub repo'''
    g = github.Github(GITHUB_USER, GITHUB_TOKEN)
    u = g.get_user()
    r = u.get_repo(REPO_NAME)
    import pdb; pdb.set_trace()
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


def upload(tag, path):
    '''Attaches a file to a tag'''
    pass
