from math import sin, cos
# from scipy.optimize import newton
import matplotlib.pyplot as plt
import pylab

f = lambda x: (x ** 3) + (2 * x ** 2) + (8 * x) + 1 + (12 * sin(x)) - (8 * cos(x))
# f = lambda x: 2 * x**2 + x * (2 / 3) - 1
f_lim = (-10, 10)


def bisection_method(function: callable, limits: tuple, precision: float) -> tuple:
    """
    Решение линейного уравнения методом половинного деления
    :param function: функция, уравнение
    :param limits: кортеж с лимитами уравнения
    :param precision: точность вычисления (чем ближе к 0, тем точнее)
    :return: корень уравнения и количество итераций
    :rtype: tuple
    """
    lim_1, lim_2 = limits[0], limits[1]
    returned = (lim_1 + lim_2) / 2
    counter = 0
    while abs(function(returned)) >= precision:
        returned = (lim_1 + lim_2) / 2

        if function(lim_1) * function(returned) < 0:
            lim_2 = returned
        else:
            lim_1 = returned
        counter += 1
    return returned, counter


def secant_method(function: callable, limits: tuple, precision: float) -> tuple:
    """
    Решение линейного уравнения методом хорд
    :param function: функция, уравнение
    :param limits: кортеж с лимитами уравнения
    :param precision: точность вычисления (чем ближе к 0, тем точнее)
    :return:
    """
    next_x, previous_x, current_x = 0, limits[0], limits[1]
    counter = 0
    while abs(next_x - current_x) > precision:
        temp = next_x
        next_x = current_x - function(current_x) * (previous_x - current_x) / (
                function(previous_x) - function(current_x))
        previous_x = current_x
        current_x = temp
        counter += 1
    return next_x, counter


def newton_method(function: callable, limits: tuple, precision: float) -> tuple:
    """
    Решение линейного уравнения методом ньютона
    :param function:
    :param limits:
    :param precision:
    :return:
    """
    pass


def main():
    bisection_iter = [bisection_method(f, f_lim, 10**-i)[1] for i in range(324)]
    print('Биитер - готово')
    print(bisection_iter)
    bisection_precision = [bisection_method(f, f_lim, 10**-i)[0] for i in range(324)]
    print('Бипре - готово')
    print(bisection_precision)
    secant_iter = [secant_method(f, f_lim, 10**-i)[1] for i in range(324)]
    print('Секитер - готово')
    print(secant_iter)
    secant_precision = [secant_method(f, f_lim, 10**-i)[0] for i in range(324)]
    print('Секпре - готово')
    print(secant_precision)

    plt.style.use('ggplot')
    pylab.subplot(1, 2, 1)
    pylab.plot(bisection_iter, label='Зависимость количества итераций метода бисекции от точности')
    pylab.plot(secant_iter, label='Зависимость количества итераций метода секущих от точности')
    pylab.title('Сравнение количества итераций методами бисекций и секущих')
    pylab.subplot(1, 2, 2)
    pylab.plot(bisection_precision, label='Значения метода бисекции')
    pylab.plot(secant_precision, label='Значение метода секущих')
    pylab.title('Сравнение значений двух методов')
    pylab.show()
