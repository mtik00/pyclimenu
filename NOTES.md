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
*   Create a tag:  
    `fab git.tag`
*   Create a GitHub release:  
    `TBD`
*   Build the packages:  
    `fab build`  
*   Upload the tarball to GitHub:  
    `fab gh.upload:"v1.1.0","dist/climenu-1.1.0.tar.gz"`
*   Upload the release to Pypi:  
    `fab pypi.upload`