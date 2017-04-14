#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
This is the "test" submenu.
'''
import climenu

@climenu.group(title='Test Menu')
def test_menu(): pass

@test_menu.menu(title='Run test #1')
def test_one():
    pass

@test_menu.menu(title='Run test #2')
def test_two():
    pass

@test_menu.menu(title='Run test #3')
def test_three():
    pass

@test_menu.menu(title='Run test #4')
def test_four():
    pass