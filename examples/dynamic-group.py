from functools import partial
import climenu


def print_var(variable):
    '''print the variable'''
    print(str(variable))


def build_items(count):
    # In this example, we're generating menu items based on some
    # thing that's determined at runtime (e.g. files in a directory).

    # For this case, we're simply using `xrange` to generate a range of
    # items.  The function that eventually gets called takes 1 argument.
    # Therefore, we need to use ``partial`` to pass in those arguments at
    # runtime.

    items = []
    for index in xrange(count):
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


if __name__ == '__main__':
    climenu.run()
