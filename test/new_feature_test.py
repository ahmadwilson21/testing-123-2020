# testing-123-2020/test/my_test.py

from app.new_feature import announce


def announce_test():
    result = announce()
    assert result == "Hello World"