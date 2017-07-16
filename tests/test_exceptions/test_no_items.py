import climenu
import pytest


def test_run(monkeypatch):
    def mockreturn(prompt):
        '''t'''
        return climenu.settings.back_values[0]

    monkeypatch.setattr(climenu, 'get_user_input', mockreturn)

    with pytest.raises(ValueError):
        climenu.run()
