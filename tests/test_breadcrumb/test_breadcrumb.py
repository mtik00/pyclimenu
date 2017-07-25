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
import re
import sys
import pytest
import climenu

if sys.version_info[0] < 3:
    import __builtin__


climenu.settings.breadcrumbs = True
climenu.settings.breadcrumb_join = ' | '


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


###############################################################################
def test_run_full(monkeypatch, capsys):

    items = [
        '2',  # Main Menu -- Test Functions
        '0',  # Back to Main Menu
        '2',  # Main Menu -- Test Functions
        '3',  # Test Functions -- Another testing menu
        '0',  # Back to Test Functions
        '3',  # Test Functions -- Another testing menu
        '1',  # Another testing menu -- Run test #3
        '',  # Press Enter to continue
        '0',  # Back to Test Functions
        '0',  # Back to Main Menu
        'q'  # Main Menu -- quit
    ]
    my_sequence = (x for x in items)

    def user_input(prompt=None):
        user_input.calls += 1
        return next(my_sequence)

    user_input.calls = 0
    monkeypatch.setattr(climenu, 'get_user_input', user_input)

    with pytest.raises(SystemExit):
        climenu.run()

    assert user_input.calls == len(items)

    out, err = capsys.readouterr()

    assert not err

    re_menus = re.compile('''
    ^main\smenu.*?
    Main\sMenu\s|\sTest\sFunctions.*?
    Main\sMenu.*?
    Main\sMenu\s|\sTest\sFunctions.*?
    Main\sMenu\s|\sTest\sFunctions\s|\sAnother\stesting\smenu.*?
    Main\sMenu\s|\sTest\sFunctions.*?
    Main\sMenu\s|\sTest\sFunctions\s|\sAnother\stesting\smenu.*?
    Main\sMenu\s|\sTest\sFunctions\s|\sAnother\stesting\smenu.*?
    Main\sMenu\s|\sTest\sFunctions.*?
    main\smenu.*?
    $
    ''', re.IGNORECASE | re.VERBOSE | re.DOTALL)

    print(out)
    assert re_menus.match(out)
