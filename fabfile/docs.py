#!/usr/bin/env python2.7
# coding: utf-8
'''
This module is used to manage the project documentation
'''

# Imports #####################################################################
import os

from fabric.api import task


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '14-JUL-2017'


# Globals #####################################################################
def _null():
    return True


@task
def serve():
    '''Auto build & serve the documentation'''
    command = 'sphinx-autobuild %s %s' % ('docs', r'docs\_build\html')
    print command
    os.system(command)
