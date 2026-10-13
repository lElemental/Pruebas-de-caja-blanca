import pytest
from process import process

@pytest.mark.statement
@pytest.mark.parametrize("values, expected", [
    ([12, 4, 3], 9),  # 12 (>10, suma 12) -> 4 (<=10, resta 4 = 8) -> 3 (impar, suma 1 = 9)
])
def test_statement_coverage(values, expected):
    assert process(values) == expected