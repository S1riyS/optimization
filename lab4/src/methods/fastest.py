from os import name

from methods.method import IMethod
from models.function import Function
from models.result import Result
from models.vector import Vector


class FastestMethod(IMethod):
    name = "Метод наискорейшего спуска"

    def __init__(self, function: Function, point: Vector, epsilon: float):
        super().__init__(function, point, epsilon)
        self.step = self.epsilon

    def solve(self) -> Result:
        iterations = 1
        while True:
            # print("Шаг", iterations)

            # Get normalized gradient direction vector
            S: Vector = self.function.gradient(self.point) / self.function.gradient_magnitude(self.point)
            # print("Point:", self.point)
            # print(f"Gradient: {self.function.gradient(self.point)}")
            # print(f"Gradient magnitude: {round(self.function.gradient_magnitude(self.point), 5)}")
            # print("Направление", S)

            # Move in the direction of the gradient until we hit the minimum
            lambda_step = 0.0
            while self.function.f(self.point - S * self.step) <= self.function.f(self.point):
                self.point = self.point - S * self.step
                lambda_step += self.step

            # print("Lambda =", round(lambda_step, 5))
            # print(f"f(x_k + S * lambda_step) = {round(self.function.f(self.point), 5)}")

            # Check if we reached the minimum
            if abs(self.function.gradient_magnitude(self.point)) < self.epsilon or lambda_step == 0:
                break

            iterations += 1
            # print()

        return Result(self.point, iterations)
