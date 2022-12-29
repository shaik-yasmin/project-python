import pytest
@pytest.fixture
def numbers():
    x,y,z=10,20,30
    return [x,y,z]
def test_function1(numbers):
    a = 10
    assert numbers[0] == a
@pytest.mark.skip
def test_function2(numbers):
    a="x"
    assert numbers[1] == a
@pytest.mark.xfail
def test_function3(numbers):
    a = 0
    assert numbers[1] == a

