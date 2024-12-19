#testsi
import pytest
from proyecto import personaje


@pytest.mark.caracteristicavalida
def test_caracteristica_valida():
    assert personaje("hombre") == "Si"