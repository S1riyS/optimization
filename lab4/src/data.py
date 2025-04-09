from models.vector import Vector


def f(point: Vector) -> float:
    x1, x2 = point.coords
    return 4 * x1**2 + 5 * x2**2 - 3 * x1 * x2 + 9 * x1 - 2 * x2


def df_dx1(point: Vector) -> float:
    x1, x2 = point.coords
    return 8 * x1 - 3 * x2 + 9


def df_dx2(point: Vector) -> float:
    x1, x2 = point.coords
    return 10 * x2 - 3 * x1 - 2


def d2f_dx1dx1(point: Vector) -> float:
    return 8


def d2f_dx2dx2(point: Vector) -> float:
    return 10
