#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This module is used to create *simple* menu-based CLI programs in Python.

This package is **highly** inspired by Click (http://click.pocoo.org).
'''

# Imports #####################################################################
from __future__ import print_function
import os
import sys

# Metadata ####################################################################
__author__ = 'Timothy McFadden'
__creationDate__ = '06-APR-2017'
__version__ = '1.5.0'


# Globals #####################################################################
__all__ = [
    'menu', 'group', 'settings', 'colors',
]
(IS_WIN, IS_LIN) = ('win' in sys.platform, 'lin' in sys.platform)
MENU_ITEMS = []
TITLE_BREADCRUMBS = []
PRESELECTED_MENU = None


class Settings(object):
    '''
    This class is used to store the settings for ``climenu``.
    '''
    clear_screen = True
    text = {
        'main_menu_title': 'Main Menu',
        'main_menu_prompt': 'Enter the selection ([{q}] to quit): ',
        'submenu_prompt': 'Enter the selection ([{back}] to return, {q} to quit): ',
        'invalid_selection': 'Invalid selection.  Please try again. ',
        'continue': 'Press Enter to continue: ',
    }

    # Add ``''`` to this list to go back one level if the user doesn't
    # enter anything
    back_values = ['0']

    # Change this to the character or phrase that will immediately exit the
    # menu.
    quit_value = 'q'

    # Change this to modify the process exit code when the user quits.
    quit_exit_code = 0

    # Set this to true if you are using colors but need to disable them
    # (e.g. a platform you use doesn't support it)
    disable_colors = False

    # Change the title of the menus to use *breadcrumbs*.
    # For example, titles would be "Main Menu > Submenu 1 > Submenu 2"
    breadcrumbs = False
    breadcrumb_join = ' > '

    def get_submenu_prompt(self):
        return self.text['submenu_prompt'].format(
            back=", ".join([x or '""' for x in self.back_values]),
            q=self.quit_value
        )

    def get_main_menu_prompt(self):
        return self.text['main_menu_prompt'].format(
            q=", ".join([x or '""' for x in self.back_values + [self.quit_value]]),
        )


settings = Settings()  # pylint: disable=C0103


def _show_title(menu_group=None):
    if settings.breadcrumbs:
        print(settings.breadcrumb_join.join(TITLE_BREADCRUMBS))
    elif menu_group:
        print(menu_group.title)
    else:
        print(settings.text['main_menu_title'])


def _show_main_menu(menu_items, break_on_invalid=False):
    '''Show the main menu and return the selected item.'''

    while True:
        _show_title()

        for index, menu_group in enumerate(menu_items):
            print("%2i : %s" % (index + 1, menu_group.title))

        print()
        value = get_user_input(settings.get_main_menu_prompt())

        if value.lower() == settings.quit_value:
            return settings.quit_value
        elif value.lower() in settings.back_values:
            return None

        if not(value.isdigit()) or (int(value) <= 0) or (int(value) > len(menu_items)):
            print(settings.text['invalid_selection'])

            if break_on_invalid:
                break

            continue  # pragma: no cover (covered in `test_nested`)

        return menu_items[int(value) - 1]


def _show_group_menu(menu_group, break_on_invalid=False):
    '''Show a submenu and return the selected item.'''
    while True:
        _show_title(menu_group)

        if menu_group.subtitle:
            print(menu_group.subtitle)

        submenu_items = menu_group.get_items()
        for index, submenu in enumerate(submenu_items):
            print("%2i : %s" % (index + 1, submenu.title))

        print()
        value = get_user_input(settings.get_submenu_prompt())

        if value.lower() == settings.quit_value:
            return settings.quit_value
        elif value.lower() in settings.back_values:
            return None

        if not(value.isdigit()) or (int(value) > len(list(submenu_items))):
            print(settings.text['invalid_selection'])

            if break_on_invalid:
                break

            continue  # pragma: no cover (covered in `test_nested`)

        return submenu_items[int(value) - 1]


def run(preselected_menu=None):
    '''
    Runs the menuing system.
    '''
    global PRESELECTED_MENU
    menu_stack = []
    current_group = None
    TITLE_BREADCRUMBS.append(settings.text['main_menu_title'])

    if preselected_menu:
        PRESELECTED_MENU = (x for x in preselected_menu)

    if not MENU_ITEMS:
        raise ValueError("No menu items defined")

    while True:
        # Clear the screen in-between each menu
        if settings.clear_screen:
            clear_screen()

        if not current_group:
            menu_item = _show_main_menu(MENU_ITEMS)
            if not menu_item:
                break
        else:
            menu_item = _show_group_menu(current_group)

        if menu_item == settings.quit_value:
            sys.exit(settings.quit_exit_code)

        # We move back through previous menus by returning None from
        if (not menu_item) and menu_stack:
            # Pop the current menu and discard it
            menu_stack.pop()

            # If there's still something in the stack, we want to show that
            # menu.
            if menu_stack:
                current_group = menu_stack.pop()

            # Pop-off the old menu's title
            TITLE_BREADCRUMBS.pop()

            continue  # pragma: no cover

        # Check for a sub-menu.  Sub-menu's don't
        # have a callback, so just set the current
        # group and loop.
        if isinstance(menu_item, MenuGroup):
            menu_stack += [current_group, menu_item]
            TITLE_BREADCRUMBS.append(menu_item.title)
            current_group = menu_item
            continue  # pragma: no cover

        # If we should show the *main* menu, then
        # ``menu_item`` will be None here.
        if menu_item:
            menu_item.callback()
            get_user_input(settings.text['continue'])


def clear_screen():
    '''Clears the terminal window'''
    if IS_WIN:
        os.system('cls')
    elif IS_LIN:
        os.system('clear')
    else:
        raise NotImplementedError(
            "Your platform has not been implemented: %s" % sys.platform)


def get_user_input(prompt=None):
    '''
    Prompt the user for input.

    :param str prompt: The text to show the user
    :param var test_value: If this is not none, the user will not be prompted
        and this value is returned.
    '''
    global PRESELECTED_MENU
    result = None

    if prompt:
        print(prompt, end='')

    if PRESELECTED_MENU:
        try:
            result = next(PRESELECTED_MENU)
            return result
        except StopIteration:
            PRESELECTED_MENU = None

    if sys.version_info[0] == 2:
        result = raw_input()
    else:
        result = input()

    return result


def first_line(text):
    '''
    Returns just the first line in a docstring.
    '''
    return text.splitlines()[0].strip()


class Menu(object):
    '''A sinlge menu item with a callback'''
    def __init__(self, title, callback):
        self.callback = callback
        self._title = title

    def __str__(self):
        return '<Menu "%s">' % self._title

    @property
    def title(self):
        if callable(self._title):
            return self._title()

        return str(self._title)


class MenuGroup(object):
    '''A group of Menu items'''
    def __init__(
        self, title, menus=None, items_getter=None, items_getter_args=None,
        items_getter_kwargs=None, subtitle=None
    ):
        self._title = title
        self._subtitle = subtitle
        self.menus = menus or []
        self.items_getter = items_getter

        self.items_getter_args = items_getter_args if items_getter_args is not None else []
        self.items_getter_kwargs = items_getter_kwargs if items_getter_kwargs is not None else {}

    def __str__(self):
        return '<MenuGroup "%s">' % self.title

    @property
    def title(self):
        if callable(self._title):
            return self._title()
        else:
            return self._title

    @property
    def subtitle(self):
        if callable(self._subtitle):
            return self._subtitle()

        return self._subtitle

    def get_items(self):
        '''
        Return the list of menu items in this group.
        '''
        if self.items_getter:
            return [
                Menu(title, callback) for (title, callback) in self.items_getter(*self.items_getter_args, **self.items_getter_kwargs)
            ]

        return self.menus

    def menu(self, *args, **kwargs):  # pylint: disable=W0613
        '''Decorator to add a menu item to our list'''
        def decorator(decorated_function):
            '''create a menu item decorator'''
            menu_ = Menu(
                kwargs.get('title') or first_line(decorated_function.__doc__),
                callback=decorated_function)
            self.menus.append(menu_)
            return menu_
        return decorator

    def group(self, *args, **kwargs):  # pylint: disable=W0613
        '''Decorator to add a menu group to our list'''
        def decorator(decorated_function):
            '''create a menu group decorator'''
            menu_ = MenuGroup(
                kwargs.get('title') or first_line(decorated_function.__doc__),
                items_getter=kwargs.get('items_getter'),
                items_getter_args=kwargs.get('items_getter_args'),
                items_getter_kwargs=kwargs.get('items_getter_kwargs'),
                subtitle=kwargs.get('subtitle'))
            self.menus.append(menu_)
            return menu_
        return decorator


def group(
    title=None, items_getter=None, items_getter_args=None,
    items_getter_kwargs=None, subtitle=None
):
    '''A decorator to create a new MenuGroup'''
    def decorator(decorated_function):
        '''create a menu group decorator'''
        group_ = MenuGroup(
            title or first_line(decorated_function.__doc__),
            items_getter=items_getter,
            items_getter_args=items_getter_args,
            items_getter_kwargs=items_getter_kwargs,
            subtitle=subtitle)
        MENU_ITEMS.append(group_)
        return group_
    return decorator


def menu(title=None):
    '''A decorator to create a single menu item'''
    def decorator(decorated_function):
        '''create a menu item decorator'''
        menu_ = Menu(
            title or first_line(decorated_function.__doc__), callback=decorated_function)
        MENU_ITEMS.append(menu_)
        return menu_
    return decorator


class ANSIColors(object):
    '''
    A class to format strings with ANSI color codes.

    The codes available are only the "first 8" color codes.  See here for
    more information:
    https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
    '''
    (black_code, red_code, green_code, yellow_code, blue_code,
     magenta_code, cyan_code, white_code) = range(8)
    fg_code = 3
    bg_code = 4

    def black(self, text, bg=False, bright=False):
        return self._wrap(text, self.black_code, bg=bg, bright=bright)

    def red(self, text, bg=False, bright=False):
        return self._wrap(text, self.red_code, bg=bg, bright=bright)

    def green(self, text, bg=False, bright=False):
        return self._wrap(text, self.green_code, bg=bg, bright=bright)

    def yellow(self, text, bg=False, bright=False):
        return self._wrap(text, self.yellow_code, bg=bg, bright=bright)

    def blue(self, text, bg=False, bright=False):
        return self._wrap(text, self.blue_code, bg=bg, bright=bright)

    def magenta(self, text, bg=False, bright=False):
        return self._wrap(text, self.magenta_code, bg=bg, bright=bright)

    def cyan(self, text, bg=False, bright=False):
        return self._wrap(text, self.cyan_code, bg=bg, bright=bright)

    def white(self, text, bg=False, bright=False):
        return self._wrap(text, self.white_code, bg=bg, bright=bright)

    def _wrap(self, text, color_code, bg=False, bright=False):
        if settings.disable_colors:
            return text

        return "\033[{fgbg}{code}{bright}m{text}\033[0m".format(
            fgbg=self.bg_code if bg else self.fg_code,
            code=color_code,
            text=text,
            bright=";1" if bright else ""
        )


colors = ANSIColors()
