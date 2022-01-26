import operaciones


def test_operaciones():
    assert operaciones.suma(3, 3) == 6
    assert operaciones.suma(-3, 3) == 0
    assert operaciones.suma(-3, -3) == -6
