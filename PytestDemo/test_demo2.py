import pytest

@pytest.mark.math
def test_addition():
    assert 1 + 1 == 2

@pytest.mark.string
def test_uppercase():
    assert "hello".upper() == "HELLO"
@pytest.mark.skip
def test_unmarked():
    assert True