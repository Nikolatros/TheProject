def get_value(x):
    """
    Находит значение функции в точке

    Args:
        x (float): точка, в которой хотим полуить значение

    Returns:
        float: Значение функции в этой точке
    """    
    if x <= -2:
        return -x - 2    
    elif -2 < x <= -1:
        return (1 - (x + 1)**2)**0.5
    elif -1 < x <= 1:
        return 1.
    elif 1 < x <= 2:
        return -2*x + 3
    elif x > 2:
        return -1.


def lab2_1():
    while 1:
        try: 
            x = float(input('Введите x = '))
        except ValueError:
            break
        print(f'x = {x}, y = {get_value(x)}')


def y_1(x, r):
    """
    Находит значение функции в точке X, с учётом параметра r

    Args:
        x (float): точка, в которой хотим полуить значение
        r (float): параметр функции

    Returns:
        float: Значение функции в этой точке, с учётом параметра
    """    
    return -x - r


def y_2(x, r):
    """
    Находит значение функции в точке X, с учётом параметра r

    Args:
        x (float): точка, в которой хотим полуить значение
        r (float): параметр функции

    Returns:
        float: Значение функции в этой точке, с учётом параметра
    """ 
    return (r**2 - x**2)**0.5


def lab2_2():
    r = float(input('Введите R = '))
    y_0 = 0
    while 1:
        x = float(input('x = '))
        y = float(input('y = '))
        belong = ((-r <= x <= 0) and (y_1(x, r) <= y <= y_0)) or ((0 <= x <= r) and (y_0 <= y <= y_2(x, r)))
        print(f'Точка ({x};{y})'+[' НЕ ', ' '][belong]+'входит')

lab2_1()
lab2_2()
