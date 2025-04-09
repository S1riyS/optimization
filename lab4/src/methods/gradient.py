from methods.method import IMethod
from models.function import Function
from models.result import Result
from models.vector import Vector


class GradientMethod(IMethod):
    name = "Метод градиентного спуска"

    def __init__(self, function: Function, point: Vector, epsilon: float):
        super().__init__(function, point, epsilon)

        self.step = 0.05

    def solve(self) -> Result:
        M = self.point

        iterations = 1
        while True:
            # print(f"Шаг {iterations}")
            # Apply gradient descent to each coordinate
            new_coords = M.coords[::]
            for i in range(self.point.dim):
                df = self.function.derivatives[i][0]  # Take first derivative of i-th coordinate
                new_coords[i] = M.coords[i] - self.step * df(M)
                # print(f"Координата {i}:")
                # print(
                #     f"df = {round(df(M), 5)}, h * df = {round(self.step * df(M), 5)}, x_n={round(M.coords[i])}, new_coord = {round(new_coords[i], 5)}"
                # )
            M = Vector(*new_coords)

            # Check if we reached the minimum
            if self.function.gradient_magnitude(M) < self.epsilon:
                break

            iterations += 1

        return Result(M, iterations)
