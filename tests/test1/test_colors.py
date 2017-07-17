#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
import climenu


def test_all_colors():
    fg_code = '[3'
    bg_code = '[4'

    for color in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
        for bg in [True, False]:
            for bright in [True, False]:
                func = getattr(climenu.colors, color)
                value = func(text='testing', bg=bg, bright=bright)
                assert value.startswith('\033')
                assert 'testing\033' in value
                if bg:
                    assert bg_code in value
                else:
                    assert fg_code in value


def test_black():
    assert climenu.colors.black('test')


def test_red():
    assert climenu.colors.red('test')


def test_green():
    assert climenu.colors.green('test')


def test_yellow():
    assert climenu.colors.yellow('test')


def test_blue():
    assert climenu.colors.blue('test')


def test_magenta():
    assert climenu.colors.magenta('test')


def test_cyan():
    assert climenu.colors.cyan('test')


def test_white():
    assert climenu.colors.white('test')


def test_disable():
    climenu.settings.disable_colors = True
    assert climenu.colors.black('test') == 'test'
