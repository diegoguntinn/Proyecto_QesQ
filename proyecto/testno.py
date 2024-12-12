#testno
import pytest
from proyecto import personaje

@pytest.mark.caracteristaerror
def test_caracteristica_error():
    assert personaje("ojos cabeza") == "No" 