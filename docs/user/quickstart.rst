.. _quickstart:

Quickstart
==========

First, make sure that ``climenu`` is :ref:`installed <install>`

The easiest way to use ``climenu`` is to create a *flat* menu like so:

.. code-block:: python

    import climenu

    @climenu.menu()
    def build_packages():
        '''Build packages'''
        # TODO: Call the build scripts here!
        print('built the packages!')

    @climenu.menu()
    def build_release():
        '''Build release'''
        # TODO: Call the build scripts here!
        print('built the release!')


    if __name__ == '__main__':
        climenu.run()

When you run this code, you will see the following menu::

    Main Menu
    1 : Build packages
    2 : Build release
    
    Enter the selection (0 to exit):

You can see that ``climenu`` is using the function docstring for the menu
text.