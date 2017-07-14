#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
import climenu


@climenu.menu()
def build_package():
    '''Build the package'''
    return True


@climenu.menu()
def build_release():
    '''Build the release'''
    return True


@climenu.menu()
def func_1():
    '''Run test #1'''
    return True


# Here's an example of the menu title being different from the function
# docstring.
@climenu.menu(title='Run test #2')
def func_2():
    '''This function tests functionality 1.2.3'''
    return True


###############################################################################
def test_module_funcs():
    '''hack coverage for this test function'''
    assert build_package.callback()
    assert build_release.callback()
    assert func_1.callback()
    assert func_2.callback()


def test_items():
    '''Test for only the main items'''
    items = [x for x in climenu.MENU_ITEMS if type(x) is climenu.Menu]
    assert len(items) == 4


def test_item_titles():
    '''Test the titles of all items'''
    items = [x for x in climenu.MENU_ITEMS if type(x) is climenu.Menu]
    assert items[0].title == 'Build the package'
    assert items[1].title == 'Build the release'
    assert items[2].title == 'Run test #1'
    assert items[3].title == 'Run test #2'


def test_groups():
    '''We shouldn't have any groups'''
    groups = [x for x in climenu.MENU_ITEMS if type(x) is climenu.MenuGroup]
    assert len(groups) == 0


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
