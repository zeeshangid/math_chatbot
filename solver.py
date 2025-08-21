import re
from typing import Dict, List


def solve_equation(equation: str) -> Dict[str, List[float]]:
    """Solve a linear equation of the form ax + b = c and show steps.

    Only supports single variable equations with integer coefficients.
    """
    equation = equation.replace(" ", "")
    pattern = r"^([+-]?\d*)x([+-]\d+)?=([+-]?\d+)$"
    match = re.fullmatch(pattern, equation)
    if not match:
        raise ValueError("Equation must be in the form ax + b = c")

    a_str, b_str, c_str = match.groups()
    a = int(a_str) if a_str not in ("", "+", "-") else (1 if a_str in ("", "+") else -1)
    b = int(b_str.replace(" ", "")) if b_str else 0
    c = int(c_str)

    steps = [f"Original equation: {a}x + {b} = {c}"]
    steps.append(f"Subtract {b} from both sides: {a}x = {c - b}")
    steps.append(f"Divide both sides by {a}: x = {(c - b)/a}")
    solution = [(c - b)/a]
    return {"steps": steps, "solution": solution}
