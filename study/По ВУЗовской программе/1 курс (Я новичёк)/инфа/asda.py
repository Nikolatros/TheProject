def number(x:float):
    if 1 <= x <= 3:
        s = input('Введите строку:\n')
        n = int(input('Введите чило повторов строки:\n'))
        for _ in range(n):
            print(s)
    elif 4 <= x <= 6:
        m = int(input('Введите степень, в которуб нужно возвести чсило:\n'))
        print(x**m)
    elif 7 <= x <= 9:
        for _ in range(10):
            x += 1
            print(x)
    else:
        print('Ошибка ввода')


def where_to_go(age: int):
    if 0 < age <= 7:
        print('Вам в детский сад')
    elif 7 < age <= 18:
        print('Вам в школу')
    elif 18 < age <= 25:
        print('Вам в профессиональное учебное заведение')
    elif 25 < age <= 60:
        print('Вам на работу')
    elif 60 < age <= 120:
        print('Вам предоставляется выбор')
    elif  0 >= age or age > 120:
        print('Ошибка! Эта программа для людей!')


x = float(input('Введите чило от 1 до 9:\n'))
number(x)

print('Общество в начале XXI века')
age = int(input('Ваш возраст:\n'))
where_to_go(age)
