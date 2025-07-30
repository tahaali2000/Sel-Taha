import pytest

@pytest.mark.math
def test_multiplication():
    assert 2 * 3 == 6

@pytest.mark.string
def test_lowercase():
    assert "WORLD".lower() == "Wrld"

def test_unmarked():
    assert True