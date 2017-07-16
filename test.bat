coverage run -p -m py.test tests/test1
coverage run -p -m py.test tests/test_nested
coverage run -p -m py.test tests/test_exceptions
coverage combine
coverage report -m --include=climenu.py