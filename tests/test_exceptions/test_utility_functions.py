import sys

import pytest

import climenu


def test_clear_screen():
    (is_win, is_lin) = ('win' in sys.platform, 'lin' in sys.platform)
    climenu.IS_WIN = False
    climenu.IS_LIN = False

    with pytest.raises(NotImplementedError):
        climenu.clear_screen()

    (climenu.IS_WIN, climenu.IS_LIN) = (is_win, is_lin)
