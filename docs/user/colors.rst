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

The functions in ``climenu.colors.*`` return strings that contain the ANSI codes
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

Disabling Colors
----------------

You can disable colors completely by using
``climenu.settings.disable_colors = True`` in your code.  This would only be
needed in cases where you are using colors in some parts of the code, but you
know you are running on a platform that doesn't support ANSI color codes.

Why is "yellow" showing up as orange?
-------------------------------------

That threw me too... A short explaination is given on `wikipedia
<https://en.wikipedia.org/wiki/ANSI_escape_code#cite_note-16>`_.  If any of
this make sense to you, good on ya!

    On terminals based on CGA compatible hardware, such as ANSI.SYS running on
    DOS, this normal intensity foreground color is rendered as Orange. CGA RGBI
    monitors contained hardware to modify the dark yellow color to an
    orange/brown color by reducing the green component