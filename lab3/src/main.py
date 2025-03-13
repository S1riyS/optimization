from dataclasses import dataclass

from constants import EPSILON, A, B
from derivatives import F_DERIVATIVES
from methods.quadratic_approximation import solve as quadratic_approximation_solve
from typing_ import SolutionFunction


@dataclass
class Solver:
    name: str
    solve: SolutionFunction


def main():
    solvers: list[Solver] = [  # type: ignore
        Solver(name="Метод квадратичной аппроксимации", solve=quadratic_approximation_solve),
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
