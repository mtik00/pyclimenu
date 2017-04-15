#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
This sample script shows a simple **flat** menu structure.  Each menu item
will be listed on the "main menu".

We also modify some of `climenu`'s settings.
'''
from __future__ import print_function
import climenu


# Let the user press the enter key to exit the application
climenu.settings.back_values = ['0', '']
climenu.settings.text['main_menu_title'] = climenu.colors.red('Application AAA Management')


@climenu.menu(title=climenu.colors.blue('Build the package'))
def build_package():
    '''Build the package'''
    print("!!!package built!!!")
    return True


@climenu.menu(title=climenu.colors.yellow('Build the release', bright=True))
def build_releasea():
    '''Build the release'''
    print("!!!release built!!!")
    return True


@climenu.menu(title=climenu.colors.magenta('Run test #1'))
def test_1():
    '''Run test #1'''
    print("!!!test #1 pass!!!")
    return True


# Here's an example of the menu title being different from the function
# docstring.
@climenu.menu(title=climenu.colors.cyan('Run test #2'))
def test_2():
    '''This function tests functionality 1.2.3'''
    print("!!!test #2 run!!!")


if __name__ == '__main__':
    climenu.run()
