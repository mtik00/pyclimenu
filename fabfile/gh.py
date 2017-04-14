#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module holds function dealing with GitHub.
'''

# Imports #####################################################################
import os
import github


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-APR-2017'


# Globals #####################################################################
GITHUB_USER = os.environ['GH_USERNAME']
GITHUB_TOKEN = os.environ['GH_TOKEN']


def repo_list():
    '''Retrieves a list of repos'''
    g = github.Github(GITHUB_USER, GITHUB_TOKEN)
    u = g.get_user()
    print([x.name for x in u.get_repos()])
