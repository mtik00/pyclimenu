#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
import climenu


def test_black():
    climenu.colors.black('test')


def test_red():
    climenu.colors.red('test')


def test_green():
    climenu.colors.green('test')


def test_yellow():
    climenu.colors.yellow('test')


def test_blue():
    climenu.colors.blue('test')


def test_magenta():
    climenu.colors.magenta('test')


def test_cyan():
    climenu.colors.cyan('test')


def test_white():
    climenu.colors.white('test')


def test_disable():
    climenu.settings.disable_colors = True
    climenu.colors.black('test')
