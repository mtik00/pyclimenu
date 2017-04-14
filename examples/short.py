#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Short example of ``climenu``
'''
from __future__ import print_function
import climenu


@climenu.menu()
def build_packages():
    '''Build packages'''
    # TODO: Call the build scripts here!
    print('built the packages!')

@climenu.menu()
def build_release():
    '''Build release'''
    # TODO: Call the build scripts here!
    print('built the release!')


if __name__ == '__main__':
    climenu.run()
