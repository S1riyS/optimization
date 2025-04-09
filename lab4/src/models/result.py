from dataclasses import dataclass

from models.vector import Vector


@dataclass
class Result:
    answer: Vector
    iterations: int
