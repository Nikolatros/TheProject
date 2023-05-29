import random


def get_value(x:float):
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


def lab3_1():
    """
    Печатает таблицу с значениями функции на промежутке [x_start;x_finish] с заданным шагом
    """    
    x_start = float(input('x_start = '))
    x_finish = float(input('x_finish = '))
    step = float(input('step = '))
    # -3 3 0.5
    x = x_start
    print("+--------+--------+")
    print("I   X    I    Y   I")
    print("+--------+--------+")
    while x <= x_finish:
        print(f"I{x: 7.2f} I{get_value(x): 7.2f} I")
        x += step
    print("+--------+--------+")


def lab3_2():
    """
    Выводит таблицу с случайными коорлинатами точками и входят ли они в область, заданную функцией
    """    
    r = float(input('Введите R = '))    
    y_0 = 0
    print("+--------+--------+-------+")
    print("I   X    I    Y   I  RES  +")
    print("+--------+--------+-------+")
    for _ in range(20):
        x, y = random.uniform(-r, r), random.uniform(-r, r)
        if -r <= x <= 0:
            belong = (y_1(x, r) <= y <= y_0)
        elif 0 <= x <= r:
            belong =  (y_0 <= y <= y_2(x, r))
        else:
            belong = False
        print(f"I{x: 7.2f} I{y: 7.2f} I  {['NO ','YES'][belong]}  I")
    print("+--------+--------+--------+")


def mr_taylor(x, eps):
    """
    Возвращает вычисленное с помощью рядов Тейлора значение в данной точке с заданной точностью

    Args:
        x (float): заданная точка
        eps (float): точность вычисления

    Returns:
        float: искомое значение
        int: использованное количество слагаемых
    """    
    n = 1
    Arth = x
    Arth_add = Arth
    while abs(Arth_add) > eps:
        k = (1 - 2/(2*n + 3))/x**2
        Arth_add *= k
        Arth += Arth_add
        n += 1

    return Arth, n


def lab3_3():
    x_start = float(input('x_start = '))
    x_finish = float(input('x_finish = '))
    step = float(input('step = '))
    eps = float(input('eps(погрешность) = '))
    
    print("+--------+--------+-------+")
    print("I   X    I    Y   I   N   +")
    print("+--------+--------+-------+")
    
    x = x_start
    while x <= x_finish:
        Arth, n = mr_taylor(x, eps)
        print(f"I{x: 7.2f} I{Arth: 7.2f} I{n: ^7}I")
        x += step
    print("+--------+--------+-------+")


lab3_3()