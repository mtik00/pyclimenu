# climenu

This project is used to create *simple* command-line interfaces using text-based menus.

The interface loosely mimiks [click](http://click.pocoo.org).

## Documentation
*   Use `sphinx-autobuild` when changing docs (makes it much easier):  
    `sphinx-autobuild docs docs/_build/html`

## Releasing
*   Make sure everything is checked in and pushed
*   Change the version `climenu.__version__`
*   Make sure `release-notes.md` is up to date
*   Add/commit/push with `prep for vX.Y.Z release`
*   Release the package with fabric:  
    `fab release`
*   Build the packages:  
    `fab make.build`  
    `python setup.py sdist --formats gztar,zip bdist_wheel`
*   Upload with `twine`:  
    `fab upload`  
    `twine upload dist/*`