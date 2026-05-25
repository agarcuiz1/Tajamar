import pytest
from main import crear_gasto

def test_crear_gasto_valido():
    gasto = crear_gasto("Agua", 1.20)
    assert gasto["nombre"] == "Agua"
    assert gasto["precio"] == 1.20

def test_crear_gasto_invalido():
    with pytest.raises(ValueError):
        crear_gasto("", 5)

    with pytest.raises(ValueError):
        crear_gasto("Algo", -3)
