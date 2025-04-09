from re import I
from typing import List

from constants import EPSILON, STARTING_POINT
from data import d2f_dx1dx1, d2f_dx2dx2, df_dx1, df_dx2, f
from methods import coordinate_based
from methods.coordinate_based import CoodrinateBasedMethod
from methods.fastest import FastestMethod
from methods.gradient import GradientMethod
from methods.method import IMethod
from models.function import Function
from models.vector import Vector


def main() -> None:
    function = Function(
        f=f,
        derivatives=[
            [df_dx1, d2f_dx1dx1],  # x1 derivatives
            [df_dx2, d2f_dx2dx2],  # x2 derivatives
        ],
        dim=2,
    )

    methods: List[IMethod] = [
        CoodrinateBasedMethod(function=function, point=STARTING_POINT, epsilon=EPSILON),
        GradientMethod(function=function, point=STARTING_POINT, epsilon=EPSILON),
        FastestMethod(function=function, point=STARTING_POINT, epsilon=EPSILON),
    ]

    for method in methods:
        print("-" * 20)
        print(method.name)
        print(method.solve())
        print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram is stopped by user")
    # except Exception as e:
    #     print("Something went wrong")
    #     print(e)
