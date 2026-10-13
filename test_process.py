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
    ([12], 12),  # Rama: Par (True) -> Mayor a 10 (True)
    ([4], -4),   # Rama: Par (True) -> Mayor a 10 (False)
    ([3], 1),    # Rama: Par (False / Impar)
    ([], 0),     # Rama: Ciclo for vacío (sale directo)
])
def test_branch_coverage(values, expected):
    assert process(values) == expected