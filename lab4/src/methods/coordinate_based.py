import copy

from methods.method import IMethod
from methods.utils.minimize1D import newton1D
from models.function import Function
from models.result import Result
from models.vector import Vector


class CoodrinateBasedMethod(IMethod):
    name = "Метод покоординатного спуска"

    def __init__(self, function: Function, point: Vector, epsilon: float):
        super().__init__(function, point, epsilon)

    def __minimize1D(self, variable_index: int, point: Vector) -> float:
        # First derivative of i-th coordinate with all other coordinates fixed
        def df(x: float) -> float:
            new_coords = list(point.coords)
            new_coords[variable_index] = x
            return self.function.derivatives[variable_index][0](Vector(*new_coords))

        # Second derivative of i-th coordinate with all other coordinates fixed
        def ddf(x: float) -> float:
            new_coords = list(point.coords)
            new_coords[variable_index] = x
            return self.function.derivatives[variable_index][1](Vector(*new_coords))

        # Newton's method
        x = point.coords[variable_index]
        return newton1D(x, df, ddf, self.epsilon)

    def solve(self) -> Result:
        M_previous = copy.deepcopy(self.point)
        M_current = copy.deepcopy(self.point)

        iterations = 1
        while True:
            for i in range(self.point.dim):
                M_current.coords[i] = self.__minimize1D(variable_index=i, point=M_current)
                # print(M_current, self.function.f(M_current))

            # Check if we reached the minimum
            function_satisfies = abs(self.function.f(M_current) - self.function.f(M_previous)) <= self.epsilon
            coordinate_satisfies = M_current.distance(M_previous) <= self.epsilon
            # print(f"Functions diff abs: {abs(self.function.f(M_current) - self.function.f(M_previous))}")
            # print(f"Coordinates distance: {M_current.distance(M_previous)}")
            if function_satisfies or coordinate_satisfies:
                break

            M_previous = copy.deepcopy(M_current)
            iterations += 1
            # print()

        return Result(M_current, iterations)
