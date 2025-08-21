import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from solver import solve_equation


def test_solve_equation():
    result = solve_equation("2x + 1 = 5")
    assert result["solution"][0] == 2.0
    assert result["steps"][0].startswith("Original equation")
