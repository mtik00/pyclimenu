#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
This is the "build" submenu.
'''
import climenu

@climenu.group(title='Build Menu')
def build_menu(): pass

@build_menu.menu(title='Build package')
def build_package():
    pass

@build_menu.menu(title='Build release')
def build_release():
    pass
