.. _advanced:

Advanced
========


Menu Groups
+++++++++++

You can create nested menus by using ``@climenu.group``, then adding menus to
that group.

The *group* is just an empty function decorated by ``@climenu.group``:

.. code-block:: python

    import climenu

    @climenu.group()
    def build_group():
        '''Build Menu'''
        pass

Once the group is defined, you can add menu items to it by using a decorator
consisting of the function name you used to create the group, and either
``.menu`` or another ``.group``.

.. code-block:: python

    @build_group.menu()
    def build_package():
        '''Build the package'''
        # TODO: Add the actual code here
        print("I built the package!")

    @build_group.menu()
    def build_release():
        '''Build the release'''
        # TODO: Add the actual code here
        print("I built the release!")

.. CAUTION::
    The name of the decorator changed from @climenu.group to @build_group!


Running this code (``climenu.run()``) will show a single menu item for the
*main* menu::

    Main Menu
    1 : Build Menu

    Enter the selection (0 to exit):

Once the user enters ``1``, the second menu will be shown::

    Build Menu
    1 : Build the package
    2 : Build the release

    Enter the selection (0 to return):

You can have any number of groups associated with other groups.

Menu Titles
+++++++++++

``climenu`` will use the function docstring as the default text displayed
for the menu items.  This can be changed by using the ``title`` parameter to the
decorator.

For example, the following code would produce the same menus as above.  Especially
look at ``build_release()``, where both ``title`` and docstring are used:

.. code-block:: python

    import climenu

    @climenu.group(title='Build Menu')
    def build_group(): pass

    @build_group.menu(title='Build the package')
    def build_package():
        # TODO: Add the actual code here
        print("I built the package!")

    @build_group.menu(title='Build the release')
    def build_release():
        '''
        Do a bunch of stuff to build the release.

            * Copy the files
            * Run some scripts
            * Build the release
            * Copy the release to X/Y/Z
        '''
        # TODO: Add the actual code here
        print("I built the release!")

    def main():
        climenu.run()

    if __name__ == '__main__':
        main()

Mutliple Files
++++++++++++++

You can split up your menu files into multiple Python files.  This is useful if you
have lots of menus, or the menu actions are complex.

One example layout like so::

    | main.py
    | build_menu.py
    | test_menu.py

``main.py``:

.. code-block:: python

    import build_menu
    import test_menu
    import climenu

    if __name__ == '__main__':
        climenu.run()

``build_menu.py``

.. code-block:: python

    import climenu

    @climenu.group(title='Build Menu')
    def build_menu(): pass

    @build_menu.menu(title='Build package')
    def build_package():
        pass

    @build_menu.menu(title='Build release')
    def build_release():
        pass

``test_menu.py``

.. code-block:: python

    import climenu

    @climenu.group(title='Test Menu')
    def test_menu(): pass

    @test_menu.menu(title='Run test #1')
    def test_one():
        pass

    @test_menu.menu(title='Run test #2')
    def test_two():
        pass

Dynamic Menu Items
++++++++++++++++++

A ``MenuGroup`` is made up of ``Menu`` items.  Normally, you create these
menu items using the ``@climenu.menu`` decorator.  However, sometimes you don't
know what these items should be until runtime.

In this case, you can use the ``items_getter``, ``items_getter_args``, and
``items_getter_kwargs`` parameters to the ``@group`` decorator.

``items_getter`` is a callback function that returns a list of tuples in the
form ``(<item-title>, <callback-function>)``.  If this function takes arguments,
you'll need to also use some combination of ``items_getter_args`` (a list of
arguments to pass to the callback function) and ``items_getter_kwargs`` (a
dictionary of keyword arguments).

.. note::
    You will need to use :func:`functools.partial` if the function(s) you are
    returning from ``items_getter`` takes any arguments.  See example below.

``dynamic-group.py``

.. code-block:: python

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
