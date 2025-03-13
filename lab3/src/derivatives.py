from math import log


def f(x: float) -> float:
    return x**2 - 3 * x + x * log(x)


def df(x: float) -> float:
    return 2 * x - 2 + log(x)


def ddf(x: float) -> float:
    return 2 + 1 / x


F_DERIVATIVES = [f, df, ddf]
