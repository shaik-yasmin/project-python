import pytest
@pytest.mark.parametrize("a,b,c",[("a","b","ab"),("c","d","cd")])
def test_functionAdd(a,b,c):
    assert a+b == c