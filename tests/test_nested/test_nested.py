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
import pytest
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


###############################################################################
def test_main_items():
    '''There should be no items in the main menu'''
    items = [x for x in climenu.MENU_ITEMS if type(x) is climenu.Menu]
    num_items = len(items)
    assert num_items == 0


def test_groups():
    '''We should have 2 groups'''
    groups = [x for x in climenu.MENU_ITEMS if type(x) is climenu.MenuGroup]
    assert len(groups) == 2


def test_show_menu(monkeypatch):
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: '1')
    climenu._show_main_menu(climenu.MENU_ITEMS)

    # Provide the "back" item
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: climenu.settings.back_values[0])
    climenu._show_main_menu(climenu.MENU_ITEMS)

    monkeypatch.setattr(climenu, 'get_user_input', lambda x: '99')
    climenu._show_main_menu(climenu.MENU_ITEMS, break_on_invalid=True)


def test_show_submenu(monkeypatch):
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: '1')
    climenu._show_group_menu(climenu.MENU_ITEMS[1])

    # Provide the "back" item
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: climenu.settings.back_values[0])
    climenu._show_group_menu(climenu.MENU_ITEMS[1])

    monkeypatch.setattr(climenu, 'get_user_input', lambda x: climenu.settings.quit_value)
    climenu._show_group_menu(climenu.MENU_ITEMS[1])

    # Provide an invalid selection
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: '99')
    climenu._show_group_menu(climenu.MENU_ITEMS[1], break_on_invalid=True)


def test_run(monkeypatch):
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: climenu.settings.back_values[0])
    climenu.run()


def test_run_full(monkeypatch):

    my_sequence = (x for x in ['2', '3', '1', '', '0', 'q'])

    def user_input(prompt=None):
        user_input.calls += 1
        return next(my_sequence)

    user_input.calls = 0
    monkeypatch.setattr(climenu, 'get_user_input', user_input)

    with pytest.raises(SystemExit):
        climenu.run()

    assert user_input.calls == 6
