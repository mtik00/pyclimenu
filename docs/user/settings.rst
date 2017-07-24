.. _settings:

Settings
========

You can use the ``settings`` object to change the behavior and text displayed by
climenu.

You would normally change the settings after importing the library like so:

.. code-block:: python

    import climenu
    climenu.settings.clear_screen = True

Changing Behavior
+++++++++++++++++

The following parameters can be used to change how climenu operates

**clear_screen** (``bool``): Whether or not climenu clears the screen when displaying
    the menu.

**back_values** (``list``): The list of values entered by the user that will cause
    the menu to go back one level (if in a ``group``), or exit the application.

    This value defaults to ``['0']``.  If you want an empty input to also result
    in *back*, change this to ``['0', '']``.  This makes it so the user can keep
    pressing the ``Enter`` key to exit the application from any submenu.

**quit_value** (``string``): This value causes the menu system to exit
    immediately.  It's also formatted in the defaults for ``text['submenu_prompt']``
    and ``text['main_menu_prompt']``.

    For example, the default settings produce a main menu prompt that looks
    like::

        Enter the selection ([0, q] to quit):
    
    and a submenu prompt that looks like::

        Enter the selection ([0] to return, q to quit):

**quit_exit_code** (``int``): This is the exit code of the python process that
    is returned when the user *quits* the menu.

Changing Displayed Text
+++++++++++++++++++++++

The ``settings`` object has a ``text`` attribute that is a dictionary.  The values
of this dictionary are the text displayed during the course of menu operation (not
to be confused with the text displayed for a menu item).

**main_menu_title** : This is the string that is displayed at the top of the first
    menu.

**main_menu_prompt** : This is the string displayed at the bottom of the first menu
    asking the user to either select and item or 'q' to exit the application.
    This includes a special formatter ``{q}`` that displays the text
    used to quit the application.

**submenu_prompt** : This is almost the same as ``main_menu_prompt``, except the user
    is prompted to select '0' to return (as opposed to *exit*).  This includes
    two special formatting fields: ``{q}``, that displays the text used to quit
    the application, and ``{back}``, which is used to show the user what to
    enter to go back **up** on level of menu.

**invalid_selection** : This is the text presented to the user if they make an invalid
    selection.

**continue** : This is the text presented to the user after a menu item has been
    executed.

**disable_color** : Set this to `True` if you have code that uses colors, but
    you want to disable it globally.  This can be useful if you have code that
    runs on multiple platforms but you need to disable colors on an unsupported
    machine.

.. CAUTION::
    Disabling colors should come prior to any color use!  For example, if you
    use colors in the other settings (`text`, `main_menu_title`, etc).

Example
+++++++

Here's an example showing all of the options:

.. code-block:: python

    import climenu
    climenu.settings.clear_screen = False
    climenu.settings.back_values = ['0', '', 'argh!']
    climenu.settings.text['main_menu_title'] = 'My Sweet Application'
    climenu.settings.text['main_menu_prompt'] = 'Enter the selection (0 to exit the application): '
    climenu.settings.text['submenu_prompt'] = 'Enter the selection (0 to return to previous menu): '
    climenu.settings.text['invalid_selection'] = "WTH?  I don't understand... try again! "
    climenu.settings.text['continue'] = 'All done with that; Press enter to go again. '

    @climenu.menu(title='Item 1')
    def item_1(): pass