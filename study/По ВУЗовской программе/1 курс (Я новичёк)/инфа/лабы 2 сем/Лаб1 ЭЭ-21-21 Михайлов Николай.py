from math import *


def z_1(x):
    """
    Находит значение функции в точке

    Args:
        x (float): точка, в которой хотим полуить значение

    Returns:
        float: Значение функции в этой точке
    """    
    return (1 - 2*(sin(x))**2)/(1 + sin(2*x))


def z_2(x):
    """
    Находит значение функции в точке

    Args:
        x (float): точка, в которой хотим полуить значение

    Returns:
        float: Значение функции в этой точке
    """    
    return (1 - tan(x))/(1 + tan(x))


a = []
print('Введите не менее 5 значений \nВвод будет завершён, если получено НЕ число')
while True:
    try:
        a.append(float(input('Ввод данных (a: float): ')))
    except ValueError:
        break
print(*[f'\ra = {a}: z_1 = {z_1(a)}, z_2 = {z_2(a)}\n' for a in a])
