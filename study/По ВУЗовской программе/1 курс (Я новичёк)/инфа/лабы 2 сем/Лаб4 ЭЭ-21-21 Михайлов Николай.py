from random import uniform


class Lab4():
    def __init__(self):
        """
        Заполняет массив указанным количеством элементов
        """        
        self.n = int(input('Введите количество элементов массива: '))
        self.array = []
        for _ in range(self.n):
            self.array.append(uniform(-5, 5))
        print(f'Количество элементов {self.n}\nНачальное состояние:')
        print(self.array)

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
        print("Введите границы интервала [a,b]:")
        a = float(input('a(нижняя граница) = '))
        b = float(input('b(верхняя граница) = '))
        for i in range(self.n):
            if a <= self.array[i] <= b:
                del self.array[i]
                self.array.append(0)


lab4 = Lab4()

print('Минимальный по модулю элемент =', lab4.sort_for_task())
print('Минимальный по модулю элемент =', lab4.comb_sort())
print('Сумма модулей элементов, после первого отрицательного = ', lab4.sum_abs())
lab4.compress()
print('Сжатый массив\n', *lab4.array)
