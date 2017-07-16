import climenu

# Let the user press the enter key to exit the application
climenu.settings.back_values = ['0', '']
climenu.settings.text['main_menu_title'] = 'Application AAA Management'


def test_submenu_prompt():
    assert climenu.settings.get_submenu_prompt()


def test_main_menu_prompt():
    assert climenu.settings.get_main_menu_prompt()
