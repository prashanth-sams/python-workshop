import pytest


@pytest.yield_fixture()
def setup():
    print('----start----')
    yield
    print('----end----')


def test_pass(setup):
    print('pass method')


def test_fail(setup):
    print('fail method')





# pytest -v -s pytest/lesson2.py
# pytest -v -s pytest/lesson2.py::test_fail
