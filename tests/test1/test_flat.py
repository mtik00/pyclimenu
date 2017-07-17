#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
import pytest

import climenu

if sys.version_info[0] < 3:
    import __builtin__


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
    assert not groups


def test_show_menu(monkeypatch):
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: '1')
    climenu._show_main_menu(climenu.MENU_ITEMS)

    # Provide the "back" item
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: climenu.settings.back_values[0])
    climenu._show_main_menu(climenu.MENU_ITEMS)

    # Provide an invalid selection
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: '99')
    climenu._show_main_menu(climenu.MENU_ITEMS, break_on_invalid=True)


def test_get_user_input(monkeypatch):
    if sys.version_info[0] == 2:
        monkeypatch.setattr(__builtin__, 'raw_input', lambda: '3')
    else:
        monkeypatch.setitem(__builtins__, 'input', lambda: '3')

    assert climenu.get_user_input('test') == '3'


def test_clear_screen(monkeypatch):
    (is_win, is_lin) = ('win' in sys.platform, 'lin' in sys.platform)

    monkeypatch.setattr(os, 'system', lambda x: None)

    climenu.IS_WIN = True
    climenu.IS_LIN = False
    climenu.clear_screen()

    climenu.IS_WIN = False
    climenu.IS_LIN = True
    climenu.clear_screen()

    (climenu.IS_WIN, climenu.IS_LIN) = (is_win, is_lin)


def test_run(monkeypatch):

    my_sequence = (x for x in ['1', '', 'q'])

    def user_input(prompt=None):
        user_input.calls += 1
        return next(my_sequence)

    user_input.calls = 0
    monkeypatch.setattr(climenu, 'get_user_input', user_input)

    with pytest.raises(SystemExit):
        climenu.run()

    assert user_input.calls == 3
