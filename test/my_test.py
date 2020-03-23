# testing-123-2020/test/my_test.py

from app.my_script import enlarge


def test_enlarge():
    result = enlarge(3)
    assert result == 300