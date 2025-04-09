import math
from typing import List


class Vector:
    def __init__(self, *args: float):
        self.coords: List[float] = list(args)
        self.dim = len(args)

    def distance(self, other: "Vector") -> float:
        s = sum((self.coords[i] - other.coords[i]) ** 2 for i in range(self.dim))
        return math.sqrt(s)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(*(self.coords[i] + other.coords[i] for i in range(self.dim)))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(*(self.coords[i] - other.coords[i] for i in range(self.dim)))

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(*(self.coords[i] * scalar for i in range(self.dim)))

    def __truediv__(self, scalar: float) -> "Vector":
        return Vector(*(self.coords[i] / scalar for i in range(self.dim)))

    def __repr__(self) -> str:
        str_coords = []
        for coord in self.coords:
            str_coords.append(str(round(coord, 6)))
        return f"Vector({', '.join(str_coords)})"
