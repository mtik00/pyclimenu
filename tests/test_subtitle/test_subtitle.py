import re
import sys
import pytest

import climenu

if sys.version_info[0] < 3:
    import __builtin__


def build_title():
    return 'Build Menu'


def build_subtitle():
    return 'a build menu'


@climenu.group(title=build_title, subtitle=build_subtitle)
def build_group():
    pass


def package_title():
    return 'Build the package'


@build_group.menu(title=package_title)
def build_package():
    # TODO: Add the actual code here
    print("I built the package!")


@build_group.menu(title='Build the release')
def build_release():
    '''
    Do a bunch of stuff to build the release.

        * Copy the files
        * Run some scripts
        * Build the release
        * Copy the release to X/Y/Z
    '''
    # TODO: Add the actual code here
    print("I built the release!")


def test_run_preselected(monkeypatch, capsys):
    '''
    Test for `preselected_menu` running out of items followed by
    quitting the application.
    '''
    if sys.version_info[0] == 2:
        monkeypatch.setattr(__builtin__, 'raw_input', lambda: climenu.settings.quit_value)
    else:
        monkeypatch.setitem(__builtins__, 'input', lambda: climenu.settings.quit_value)

    with pytest.raises(SystemExit):
        climenu.run(['1'])

    out, err = capsys.readouterr()

    assert re.search('Build Menu\na build menu', out)
    assert package_title() in out


def main():
    climenu.run()


if __name__ == '__main__':
    main()
