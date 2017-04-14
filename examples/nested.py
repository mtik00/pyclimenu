#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
This sample script shows a simple **nested** menu structure.

There are two `group` items: `build_menu` and `test_menu`.  These two items
are shown on the main menu.  Once selected, thier respective sub-items will
be shown.

`test_menu` has a sub-menu itself, `sub_test_menu`.  That item has a single
menu item.

Notice how the decorators change from `@climenu` to `@build_menu` and
`@test_menu`.
'''
from __future__ import print_function
import climenu


###############################################################################
# Create an empty function to serve as a menu group
@climenu.group()
def build_menu():
    '''Build Functions'''
    pass


# Add this function to the `build_menu` group
@build_menu.menu()
def test():
    '''Build the package'''
    print("!!!package build!!!")
    return True


# Add this function to the `build_menu` group
@build_menu.menu()
def test2():
    '''Build the release'''
    print("!!!release build")
    return True
###############################################################################

###############################################################################
# Create an empty function to serve as a menu group
@climenu.group()
def test_menu():
    '''Test Functions'''
    pass


# Add this function to the `test_menu` group
@test_menu.menu()
def test_one():
    '''Run test #1'''
    print("!!!test #1 run!!!")
    return True


# Add this function to the `test_menu` group
@test_menu.menu()
def test_two():
    '''Run test #2'''
    print("!!!test #2 run!!!")


# Create a sub-group and add it to the `test_menu` group
@test_menu.group()
def sub_test_menu():
    '''Another testing menu'''
    pass


# Add this function to the `subsub_menu` group
@sub_test_menu.menu()
def subsub_menu1():
    '''Run test #3'''
    print("!!!test #3 run!!!")
#################################################################################

if __name__ == '__main__':
    climenu.run()
