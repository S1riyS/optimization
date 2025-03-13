"""
Метод квадратичной аппроксимации
"""

from typing_ import Math1DFunction  # type: ignore

__MAX_ITERATIONS = 10_000


def __argmin(arr: list[float]) -> int:
    min_idx = 0
    min_val = arr[0]
    for idx, val in enumerate(arr[1:], start=1):
        if val < min_val:
            min_idx = idx
            min_val = val
    return min_idx


def solve(
    f_derivatives: list[Math1DFunction],
    a: float,
    b: float,
    epsilon: float,
) -> tuple[float, float]:
    f = f_derivatives[0]
    step = 0.1

    # Шаг 1: Задаем начальные точки
    x1 = (a + b) / 2
    x2 = x1 + step
    f1, f2 = f(x1), f(x2)

    # Шаг 2: Определяем третью точку
    if f1 > f2:
        x3 = x1 + 2 * step
    else:
        x3 = x1 - step
    f3 = f(x3)

    for iteration in range(1, __MAX_ITERATIONS + 1):
        f_min = min(f1, f2, f3)
        x_min = [x1, x2, x3][__argmin([f1, f2, f3])]
        print(f"\nШаг {iteration}:")
        print(f"x1 = {x1}; x2 = {x2}; x3 = {x3}")
        print(f"f(x1) = {f1}; f(x2) = {f2}; f(x3) = {f3}")
        # print(f"x_min = {x_min}; f_min = {f_min}")

        # Шаг 4: Вычисляем точку минимума квадратичного полинома
        numerator = (x2**2 - x3**2) * f1 + (x3**2 - x1**2) * f2 + (x1**2 - x2**2) * f3
        denominator = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3

        if denominator == 0:
            print("Знаменатель равен 0. Переход к следующему шагу (x1 = x_min).")
            x1 = x_min
            x2 = x1 + step
            f1, f2 = f(x1), f(x2)
            if f1 > f2:
                x3 = x1 + 2 * step
            else:
                x3 = x1 - step
            f3 = f(x3)
            continue

        x_bar = 0.5 * numerator / denominator
        f_bar = f(x_bar)

        print(f"x_bar = {x_bar}; f_bar = {f_bar}")

        # Шаг 5: Проверяем условия окончания
        # print(f"abs((f_min - f_bar) / f_bar) = {abs((f_min - f_bar) / f_bar)}")
        # print(f"abs((x_min - x_bar) / x_bar = {abs(x_min - x_bar) / x_bar}")
        if abs((f_min - f_bar) / f_bar) < epsilon and abs((x_min - x_bar) / x_bar) < epsilon:
            print("Заданная точность достигнута. Завершаем алгоритм.\n")
            return x_bar, f_bar

        if x_bar in [x1, x3]:
            x2 = min(x_bar, x_min)
            x1 = x2 - step
            x3 = x2 + step
            f1, f2, f3 = f(x1), f(x2), f(x3)
        else:
            x1 = x_bar
            x2 = x1 + step
            f1, f2 = f(x1), f(x2)

            if f1 > f2:
                x3 = x1 + 2 * step
            else:
                x3 = x1 - step
            f3 = f(x3)

    return -1, -1
