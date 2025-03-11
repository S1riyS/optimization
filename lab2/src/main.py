from dataclasses import dataclass

from constants import EPSILON, A, B
from derivatives import F_DERIVATIVES
from methods.chord import solve as chord_solve
from methods.golden_ratio import solve as golden_ratio_solve
from methods.half_division import solve as half_division_solve
from methods.newton import solve as newton_solve
from typing_ import SolutionFunction


@dataclass
class Solver:
    name: str
    solve: SolutionFunction


def main():
    solvers: list[Solver] = [  # type: ignore
        Solver(name="Метод половинного деления", solve=half_division_solve),
        Solver(name="Метод золотого сечения", solve=golden_ratio_solve),
        Solver(name="Метод хорд", solve=chord_solve),
        Solver(name="Метод Ньютона", solve=newton_solve),
    ]

    for solver in solvers:
        print(f"===========\n\n{solver.name}:\n")

        solve = solver.solve
        x_m, y_m = solve(F_DERIVATIVES, A, B, EPSILON)

        print(f"x_m = {x_m}")
        print(f"y_m = f(x_m) = {y_m}")
        print()


if __name__ == "__main__":
    main()
