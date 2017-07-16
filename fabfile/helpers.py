#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module holds various helper functions
'''

# Imports #####################################################################
from __future__ import print_function
import os
import sys
import subprocess


# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '13-APR-2017'


# Globals #####################################################################
def user_input(prompt, default=None):
    '''Gets input from the user'''
    if sys.version_info[0] == 2:
        answer = raw_input(prompt)
    else:
        answer = input(prompt)

    return answer or default


def ex(command, cwd=None, shell=None, raise_on_nonzero=True):
    """Execute a command and return the output.  This will raise an Exception if
    the return code is non-zero.

    :param str/list command: Either a string or a list of arguments.
    :param bool shell: If None, "shell" will be determined by the type of
        `command` (str -> shell=True; list -> shell=False)
    :param bool raise_on_nonzero: Raise an exception if the return code of the
        process is not zero.
    :returns: tuple(text, returncode)
    """
    shell = shell if (shell is not None) else (type(command) is not list)

    p = subprocess.Popen(
        command, shell=shell, cwd=cwd, stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE)

    output, _ = p.communicate()

    if p.returncode and raise_on_nonzero:
        raise Exception("command failed: %s" % output)

    return (output, p.returncode)


def true(value):
    '''Since fabric task inputs are always text, we need a way to convert it
    to a boolean.
    '''
    if isinstance(value, bool):
        return value
    elif isinstance(value, basestring):
        return value.lower()[0] in ['y', 't', '1']

    # Use the default representation
    return bool(value)


def remove_directory(top, remove_top=True, filter=None):
    '''
    Removes all files and directories, bottom-up.

    :param str top: The top-level directory to clean out
    :param bool remove_top: Whether or not to delete the top
        directory when cleared.
    :param code filter: A function that returns True or False
        based on the name of the file or folder.  Returning
        True means "delete it", False means "keep it".
    '''
    if not os.path.isdir(top):
        return

    if filter is None:
        filter = lambda x: True

    for root, dirs, files in os.walk(top, topdown=False):
        for name in [x for x in files if filter(x)]:
            os.remove(os.path.join(root, name))

        for name in [x for x in dirs if filter(x)]:
            os.rmdir(os.path.join(root, name))

    if remove_top:
        try:
            os.rmdir(top)
        except OSError as e:
            print("error removing top:", e.message, file=sys.stderr)
