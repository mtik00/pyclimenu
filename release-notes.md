# v------
*   FIX: 'q' doesn't actually quit from a submenu
*   Adding the ability to pre-select menu items during `run()`
***

# v1.3.0
*   Changing the way the function docstring is used as the title.  We'll now
    run it through `.splitlines()[0].strip()`.
*   Adding support for dynamic menu items in a group.  
    For example: `@climenu.group(items_getter, items_getter_args, items_getter_kwargs)`
***

# v1.2.0
*   Adding `q` to quit the application immediately.  You no longer have to
    back all of the way out.
***

# v1.1.2
*   FIX: setup.py not compatible with Python 3.
***

# v1.1.1
*   FIX: package not included in setup.py
***

# v1.1.0
*   Adding ANSI color codes (`climenu.colors`)
***


# v1.0.0
*   Initial release.
***