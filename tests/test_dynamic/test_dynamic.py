from __future__ import print_function
from functools import partial

import climenu


def print_var(variable):
    '''print the variable'''
    print(str(variable))


def build_items(count):
    # In this example, we're generating menu items based on some
    # thing that's determined at runtime (e.g. files in a directory).

    # For this case, we're simply using `range` to generate a range of
    # items.  The function that eventually gets called takes 1 argument.
    # Therefore, we need to use ``partial`` to pass in those arguments at
    # runtime.

    items = []
    for index in range(count):
        items.append(
            (
                'Run item %i' % (index + 1),
                partial(print_var, 'Item %i' % (index + 1))
            )
        )

    return items


@climenu.menu(title='Do the first thing')
def first_thing():
    # A simple menu item
    print('Did the first thing!')


@climenu.group(items_getter=build_items, items_getter_kwargs={'count': 7})
def build_group():
    '''A dynamic menu'''
    # This is just a placeholder for a MenuGroup.  The items in the menu
    # will be dymanically generated when this module loads by calling
    # `build_items`.
    pass
################################################################################


###############################################################################
def test_main_items():
    '''There should be 1 item in the main menu'''
    items = [x for x in climenu.MENU_ITEMS if type(x) is climenu.Menu]
    num_items = len(items)
    assert num_items == 1


def test_groups():
    '''We should have 1 group'''
    groups = [x for x in climenu.MENU_ITEMS if type(x) is climenu.MenuGroup]
    assert len(groups) == 1


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


