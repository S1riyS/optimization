"""
Метод Хорд
"""

from typing_ import Math1DFunction  # type: ignore


def solve(
    f_derivatives: list[Math1DFunction],
    a: float,
    b: float,
    e: float,
) -> tuple[float, float]:
    f = f_derivatives[0]
    f_d1 = f_derivatives[1]
    f_d2 = f_derivatives[2]

    iteration = 1
    while True:
        print(f"Шаг {iteration}:")
        # Находим x по формуле
        x = a - (f_d1(a) / (f_d1(b) - f_d1(a))) * (b - a)
        y_d1 = f_d1(x)

        # print(f"f'(a) = {f_d1(a)}, f'(b) = {f_d1(b)}")
        print(f"x = {x}, f'(x) = {f_d1(x)}\n")

        # Условие остановки
        if abs(y_d1) <= e:
            break

        # Подготовка к следующей итерации
        if y_d1 > 0:
            b = x
        else:
            a = x

        iteration += 1

    print(f"\n|f'(x)| <= ε. Минимум с заданной погрешностью ε = {e} найден!")
    print(f"Минимум достигается в точке xm = {x}.")
    print(f"Значение в минимуме ym = {f(x)}.\n")

    return x, f(x)
