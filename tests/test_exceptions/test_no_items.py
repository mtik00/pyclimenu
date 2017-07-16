import climenu
import pytest


def test_run(monkeypatch):
    monkeypatch.setattr(climenu, 'get_user_input', lambda x: climenu.settings.back_values[0])

    with pytest.raises(ValueError):
        climenu.run()
