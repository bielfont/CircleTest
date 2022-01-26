import operaciones


def test_operaciones():
    assert operaciones.suma(3, 3) == 6
    assert operaciones.suma(-3, 3) == 0
    assert operaciones.suma(-3, -3) == -6


def test_operaciones2():
    assert operaciones.resta(3, 3) == 0
    assert operaciones.resta(3, 2) == 1
    assert operaciones.resta(3, 0) == 0
