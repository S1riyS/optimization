from typing import Callable

Math1DFunction = Callable[[float], float]
SolutionFunction = Callable[[list[Math1DFunction], float, float, float], tuple[float, float]]
