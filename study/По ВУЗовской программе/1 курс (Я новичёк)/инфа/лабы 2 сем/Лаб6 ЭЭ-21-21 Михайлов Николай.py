from random import randint
from random import uniform
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


def lab1():
    input_data = []
    with open('Лаб6_1_in.txt', encoding='utf-8') as r_file:
        for row in r_file:
            input_data.append(row[:-1])
    a = [float(data) for data in input_data[2:]]
    with open('Лаб6_1_out.txt', mode='w+', encoding='utf-8') as w_file:
        for a in a:
            w_file.write(f'a = {a}: z_1 = {z_1(a)}, z_2 = {z_2(a)}\n')


class Lab4():
    def __init__(self, w_file):
        """
        Заполняет массив указанным количеством элементов
        """ 
        self.w_file = w_file
        input_data = []       
        with open('Лаб6_4_in.txt', encoding='utf-8') as r_file:
            for row in r_file:
                input_data.append(int(row.split(' = ')[-1][:-1]))
        self.n, self.a, self.b = input_data
        self.array = []
        for _ in range(self.n):
            self.array.append(uniform(-5, 5))
        self.w_file.write(f'Количество элементов {self.n}\nНачальное состояние:\n')
        self.w_file.write(f'{self.array}\n')

    def sort_for_task(self):
        """
        Одним проходом вытесняет меньший по модулю элемент на постледнюю позицию массива

        Returns:
            float: меньший по модулю элемент
        """        
        array_copy = self.array
        for i in range(self.n - 1):
            if abs(array_copy[i]) < abs(array_copy[i + 1]):
                array_copy[i], array_copy[i + 1] = array_copy[i + 1], array_copy[i]
        
        return array_copy[-1]

    def comb_sort(self):
        """
        Сортирует массив по модулям элементов.
        Сортировка расчёской

        Returns:
            float: меньший по модулю элемент
        """        
        array_copy = self.array
        step = self.n
        swap = True
        
        while step > 1 and swap:
            step = max(1, int(step/1.247))
            swap = False
            for i in range(len(array_copy) - step):
                if abs(array_copy[i]) > abs(array_copy[i + step]):
                    array_copy[i], array_copy[i + step] = array_copy[i + step], array_copy[i]
                    swap = True
        
        return array_copy[0]

    def sum_abs(self):
        """
        Считает сумму модулей элементов, расположенных после первого отрицательного элемента.

        Returns:
            float: сумма модулей элементов, расположенных после первого отрицательного элемента.
        """        
        for i in range(self.n):
            if self.array[i] < 0:
                if i == self.n - 2:
                    return abs(self.array[-1])
                return sum([abs(number) for number in self.array[i+1:]])
        return 0

    def compress(self):
        """
        Сжимает массив, удаляя из него все элементы, величина которых находится в интервале [а, b]. 
        Освободившиеся в конце массива элементы заполняет нулями.

        """        

        for i in range(self.n):
            if self.a <= self.array[i] <= self.b:
                del self.array[i]
                self.array.append(0)


def lab4():
    
    with open('Лаб6_4_out.txt', mode='w+', encoding='utf-8') as w_file:
        lab4 = Lab4(w_file)
        w_file.write(f'Минимальный по модулю элемент = {lab4.sort_for_task()}\n')
        w_file.write(f'Минимальный по модулю элемент = {lab4.comb_sort()}\n')
        w_file.write(f'Сумма модулей элементов, после первого отрицательного =  {lab4.sum_abs()}\n')
        lab4.compress()
        w_file.write(f'Сжатый массив\n{lab4.array}')


class array():
    def __init__(self, n, m):
        self.n, self.m = n, m
        self.array = []
        for i in range(n):
            self.array.append([randint(-20, 20) for j in range(m)])

    def show_array(self, w_file):
        """
        Выводит на экран массив в привычном виде.
        """        
        for row in self.array:
            w_file.write('[')
            for elem in row:
                if elem % 1 == 0 or int(elem*1e3) == 0:
                    # если число целое или пренебрежимо мало(соласно точности выввода), то выводим его целую часть
                    w_file.write(f'{int(elem): ^8},')
                else:
                    w_file.write(f'{elem: ^8.3F},')
            w_file.write(']\n')

    def form_step_array(self):
        """
        Приводит массив к треугольному виду.
        Не работает, "если опорный" элемент следующей строки равен нулю.
        """        
        def row_subtraction(i, row_1, row_2):
            """
            Вычитает из строки матрицы другую,
            умноженную на такое число, чтобы разность заданных элементов строк была равна нулю.

            Args:
                i (int): индекс заданного элемента строки
                row_1 (list): строка, умножаемая на число. Вычитаемое
                row_2 (list): Уменьшаемое
            """
            if row_1[i] == 0:
                pass
            n = row_2[i]/row_1[i]
            for j in range(i, self.m):
                row_2[j] -= n*row_1[j]
            

        for i in range(min(self.n - 1, self.m)):
            # i - номер строки, с помошью которой будем занулять [i:m] элементы следущих строк
            # поэтому i должно быть меншим из (кол-во строк, не включая первую / "ширина" матрицы)
            # благодарю тамкому выбора индекса, мы можем спустить по диагонали вниз с первого элемента второй строки
            row_1 = self.array[i]
            for row_2 in self.array[i+1: ]:
                # Для всех нижестоящих строк
                row_subtraction(i, row_1, row_2)

    def number_that_row(self, limit):
        """
        Возвращает количество строк, среднее арифметическое элементов которых меньше порогового значения.


        Args:
            limit (float): пороговое значение

        Returns:
            int: количество искомых строк
        """        
        number = 0
        for row in self.array:
            average = sum(row)/self.m
            if average < limit:
                number += 1
        return number


def lab5():
    input_data = []
    
    with open('Лаб6_5_in.txt') as r_file:
        for row in r_file:
            input_data.append(int(row.split(' = ')[-1][:-1]))
    n, m, limit = input_data
    
    qwe = array(n, m) 

    with open('Лаб6_5_out.txt', mode='w+', encoding='utf-8') as w_file:
        w_file.write(f'Размерность массива {n} × {m}:\n\n')
        qwe.show_array(w_file)
        number_limit_row = qwe.number_that_row(limit=limit)
        w_file.write(f'Количество строк, среднее арифметическое элементов которых меньше порогового значения: {number_limit_row}\n')
        
        qwe.form_step_array()
        w_file.write('\nТреугольный вид:\n')
        qwe.show_array(w_file)
        number_limit_row = qwe.number_that_row(limit=limit)
        w_file.write(f'Количество строк, среднее арифметическое элементов которых меньше порогового значения: {number_limit_row}\n')


lab1()
