#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
This is a menu-driven command line application to
facilitate building and testing.
'''

import build_menu  # pylint: disable=W0611
import test_menu  # pylint: disable=W0611
import climenu


if __name__ == '__main__':
    climenu.run()