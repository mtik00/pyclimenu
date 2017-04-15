.. _colors:

Colors
======

climenu supports basic ANSI colors, including foreground, background, and
*bright*.

.. CAUTION::
    Windows may have some strange affects when using ANSI formatting codes.  It
    may not always work! YMMV

.. CAUTION::
    There's no way of knowing what color scheme your users are using in thier
    terminal.  It's best to use colors sparingly, and perhaps always define a
    background. 


ANSI Color Table
----------------

You can read more about the ANSI color table `on wikipedia
<https://en.wikipedia.org/wiki/ANSI_escape_code#Colors>`_

The supported colors are: black, red, green, yellow, blue, magenta, cyan,
and white.

Using Colors
------------

You can use the colors by *wrapping* some text with the color codes.  This
is done using the ``climenu.colors`` object.

.. code-block:: python

    import climenu

    # Print red text on the default background.
    print(
        climenu.colors.red("Hello World!")
    )


Nesting
-------

The functions in `climenu.colors.*` return strings that contain the ANSI codes
needed to format your text.  This also means that you can *nest* these calls,
or make multiple calls to create multi-formatted strings (e.g. bright-blue
text on a yellow background).

.. code-block:: python

    import climenu

    # Print bright-blue text on a yellow background
    print(
        climenu.colors.yellow(
            climenu.colors.blue("Hello World!", bright=True),
            bg=True)
    )

    # Another way to do it
    text = climenu.colors.blue("Hello World!", bright=True)
    text = climenu.colors.yellow(text, bg=True)