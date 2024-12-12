#testcierto
import pytest
from proyecto import personaje
from proyecto.state import personaje_maquina

@pytest.mark.caracteristaerror
def test_personajeacertado():
    assert personaje(personaje_maquina) == "GG ganaste"