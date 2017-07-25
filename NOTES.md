# climenu

This project is used to create *simple* command-line interfaces using text-based menus.

The interface loosely mimics [click](http://click.pocoo.org).

## Management

To manage the project, you'll need to install the project's requirements file:  
`pip install -r proj-requirements.txt`

## Documentation
*   Use `sphinx-autobuild` when changing docs (makes it much easier):  
    `sphinx-autobuild docs docs/_build/html`  
    or `fab docs.serve`

## Releasing
*   Make sure everything is checked in and pushed
*   Change the version using `fab.rev`  
    That will change both `climenu.__version__` and `docs/conf.py`
*   Make sure `release-notes.md` is up to date
*   Add/commit/push with `prep for vX.Y.Z release`
*   Create a tag:  
    `fab git.tag`
*   Do the release:  
    `fab release`