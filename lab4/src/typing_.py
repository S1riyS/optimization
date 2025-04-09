from typing import Callable, Protocol

from models.vector import Vector

Math1DFunction = Callable[[float], float]


class MathNDFunction(Protocol):
    def __call__(self, point: Vector) -> float: ...
