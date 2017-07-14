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

###############################################################################
# def test_module_funcs():
#     '''hack coverage for this test function'''
#     assert build_package.callback()
#     assert build_release.callback()
#     assert func_1.callback()
#     assert func_2.callback()


def test_main_items():
    '''There should be no items in the main menu'''
    items = [x for x in climenu.MENU_ITEMS if type(x) is climenu.Menu]
    assert len(items) == 0


# def test_item_titles():
#     '''Test the titles of all items'''
#     items = [x for x in climenu.MENU_ITEMS if type(x) is climenu.Menu]
#     assert items[0].title == 'Build the package'
#     assert items[1].title == 'Build the release'
#     assert items[2].title == 'Run test #1'
#     assert items[3].title == 'Run test #2'


def test_groups():
    '''We should have 2 groups'''
    groups = [x for x in climenu.MENU_ITEMS if type(x) is climenu.MenuGroup]
    assert len(groups) == 2


def test_show_menu(monkeypatch):
    def mockreturn(prompt):
        return '1'

    monkeypatch.setattr(climenu, 'get_user_input', mockreturn)
    climenu._show_main_menu(climenu.MENU_ITEMS)

    # Provide the "back" item
    def mockreturn2(prompt):
            return climenu.settings.back_values[0]

    monkeypatch.setattr(climenu, 'get_user_input', mockreturn2)
    climenu._show_main_menu(climenu.MENU_ITEMS)

    # Provide an invalid selection
    def mockreturn2(prompt):
            return '99'

    monkeypatch.setattr(climenu, 'get_user_input', mockreturn2)
    climenu._show_main_menu(climenu.MENU_ITEMS, break_on_invalid=True)
