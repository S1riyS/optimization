from abc import ABC, abstractmethod

from models.function import Function
from models.result import Result
from models.vector import Vector


class IMethod(ABC):
    def __init__(self, function: Function, point: Vector, epsilon: float):
        super().__init__()

        assert function.dim == point.dim

        self.function = function
        self.point = point
        self.epsilon = epsilon

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def solve(self) -> Result: ...
