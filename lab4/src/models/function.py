import math
from typing import List

from models.vector import Vector
from typing_ import MathNDFunction


class Function:
    def __init__(self, f: MathNDFunction, derivatives: List[List[MathNDFunction]], dim: int):
        self.f = f
        self.derivatives = derivatives
        self.dim = dim

        assert len(derivatives) == dim

    def gradient(self, point: Vector) -> Vector:
        return Vector(*(self.derivatives[i][0](point) for i in range(self.dim)))

    def gradient_magnitude(self, point: Vector) -> float:
        grad_square_sum = sum((self.derivatives[i][0](point)) ** 2 for i in range(self.dim))
        return math.sqrt(grad_square_sum)
