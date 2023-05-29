from random import randint


class array():
    def __init__(self, n, m):
        self.n, self.m = n, m
        self.array = []
        for i in range(n):
            self.array.append([randint(-20, 20) for j in range(m)])

    def show_array(self):
        """
        Выводит на экран массив в привычном виде.
        """        
        for row in self.array:
            print('[', end='')
            for elem in row:
                if elem % 1 == 0 or int(elem*1e3) == 0:
                    # если число целое или пренебрежимо мало(соласно точности выввода), то выводим его целую часть
                    print(f'{int(elem): ^8},', end='')
                else:
                    print(f'{elem: ^8.3F},', end='')
            print(']')

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


print('Введите размерность массива N × M:')
n = int(input('n = ')) 
m = int(input('m = '))
limit = float(input('Введите пороговое значение \nlimit = '))

qwe = array(n, m)
qwe.show_array()
number_limit_row = qwe.number_that_row(limit=limit)
print('Количество строк, среднее арифметическое элементов которых меньше порогового значения:', number_limit_row)
print('\nТреугольный вид:')
qwe.form_step_array()
qwe.show_array()
number_limit_row = qwe.number_that_row(limit=limit)
print('Количество строк, среднее арифметическое элементов которых меньше порогового значения:', number_limit_row)
