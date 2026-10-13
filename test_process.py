import pytest
from process import process

@pytest.mark.statement
@pytest.mark.parametrize("values, expected", [
    ([12, 4, 3], 9),
])
def test_statement_coverage(values, expected):
    assert process(values) == expected

@pytest.mark.branch
@pytest.mark.parametrize("values, expected", [
    ([12], 12),
    ([4], -4),
    ([3], 1),
    ([], 0),
])
def test_branch_coverage(values, expected):
    assert process(values) == expected

@pytest.mark.path
@pytest.mark.parametrize("values, expected", [
    ([], 0),               # Camino 1: Sin entrar al bucle
    ([12], 12),            # Camino 2: Bucle -> Par -> >10
    ([4], -4),             # Camino 3: Bucle -> Par -> <=10
    ([5], 1),              # Camino 4: Bucle -> Impar
    ([12, 4, 5], 9),       # Camino 5: Combinación completa en secuencia
])
def test_path_coverage(values, expected):
    assert process(values) == expected