# climenu

This project is used to create *simple* command-line interfaces using text-based menus.

The interface loosely mimiks [click](http://click.pocoo.org).

## Releasing
*   Modify `version.py`
*   Build the packages:  
    `python setup.py sdist --formats gztar,zip bdist_wheel`
*   Upload with `twine`:  
    `twine upload dist/*`