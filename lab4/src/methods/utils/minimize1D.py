import xml

from typing_ import Math1DFunction


def newton1D(x: float, df: Math1DFunction, ddf: Math1DFunction, epsilon: float) -> float:
    while abs(df(x)) > epsilon:
        x = x - df(x) / ddf(x)
    return x
