Due to the nature of the module, and the nature of pytest, we can't run all of
the tests together.

This is because pytest imports everything it finds, which modifies `climenu`
objects, which cause side affects for other tests.

We can only do:
    ```
    pytest tests\test1
    pytest tests\test2
    ```