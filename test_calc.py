import pytest
from calc import suma, resta, multiplicar, dividir


def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0


def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 5) == -5
    assert resta(-2, -3) == 1


def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 3) == -3
    assert multiplicar(0, 100) == 0


def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(-10, 2) == -5

    # Verificar excepción por división por cero
    with pytest.raises(ValueError, match="División por cero no permitida"):
        dividir(5, 0)
