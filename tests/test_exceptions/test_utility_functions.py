import sys

import pytest

import climenu


def test_clear_screen():
    is_win = sys.platform.startswith('win')
    is_nix = sys.platform.startswith('lin') or sys.platform.startswith('darwin')

    climenu.IS_WIN = False
    climenu.IS_NIX = False

    with pytest.raises(NotImplementedError):
        climenu.clear_screen()

    (climenu.IS_WIN, climenu.IS_NIX) = (is_win, is_nix)
