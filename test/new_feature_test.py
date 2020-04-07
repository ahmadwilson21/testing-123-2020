# testing-123-2020/test/my_test.py

from app.new_feature import announce


def test_announce():
    result = announce()
    assert result == "Hello World"