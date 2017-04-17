.. image:: https://travis-ci.org/mtik00/pyclimenu.svg?branch=master
    :target: https://travis-ci.org/mtik00/pyclimenu

climenu
=======
This project is used to create *simple* command-line interfaces using
text-based menus.

The interface loosely mimics `click <http://click.pocoo.org>`_ (the use of
decorators to define the interface).

Documentation is hosted `on ReadTheDocs <http://pyclimenu.rtfd.io/>`_; releases
are hosted `on pypi <https://pypi.python.org/pypi/climenu>`_.

----

Example:

.. code-block:: python

    from __future__ import print_function
    import climenu

    @climenu.menu()
    def build_release():
        '''Build release'''
        print("built the release")

    @climenu.menu()
    def build_package():
        '''Build the package'''
        print("built the package")

    if __name__ == '__main__':
        climenu.run()
