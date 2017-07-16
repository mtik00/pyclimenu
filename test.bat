FOR /F "tokens=*" %%G IN ('dir /b /a:d "tests\test*"') DO (
    echo Found %%G
    coverage run -p -m py.test tests/%%G
)

coverage combine
coverage report -m