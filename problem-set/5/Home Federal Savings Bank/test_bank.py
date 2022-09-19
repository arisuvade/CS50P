from bank import value

def main():
    test_value_1()
    test_value_2()


def test_value_1():
    assert value("Hello") == "$0"


def test_value_2():
    assert value("What's up!") == "$100"
