import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mbox


class App():
    def __init__(self, window):
        self.window = window
        # Создание главного меню
        mainmenu = tk.Menu(self.window)
        self.window.config(menu=mainmenu)
        # Создание каскадного меню "Файл"
        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label = "Создать", command=self.new_file)
        filemenu.add_command(label = "Открыть..", command=self.open_file)
        # Инициализация каскадного меню
        mainmenu.add_cascade(label="Файл", menu=filemenu)
        # Навзвание открытого файла
        self.this_file = tk.Label(window, text=" ", font='Arial 10')
        self.this_file.grid(row=0, column=0, columnspan=2, sticky='W', padx=10)
        # пункт и поиск
        self.point = tk.Entry(self.window, width= 20)
        self.point.grid(row=1, column=0, padx=10)
        self.find = tk.Button(self.window, text='Найти', command=self.find_point,)
        self.find.grid(row=1, column=1, padx=70, ipadx=10)
        # Запуск приложения
        self.window.mainloop()

    def open_file(self):
        self.filename = fd.askopenfilename(
            title="Открыть файл",
            initialdir="/",
            filetypes=(
                ("Текстовый файл", "*.txt"),
                )
            )
        # Вывод названия открытого файла
        self.this_file['text'] = self.filename.split('/')[-1]

    def find_point(self):
        # Обработка исключения
        if self.this_file['text'] == ' ':
            mbox.showerror("Ошибка", "Файл не выбран")
            return
        # Обзор файла
        self.points = []
        self.rout_names = []
        with open(f'{self.filename}', encoding='utf-8') as w_file:
            for row in w_file:
                data = row.split(';')
                self.points.append(data[:2])
                self.rout_names.append(data[2][:-1])
        required_point = self.point.get()
        if not required_point.isalpha():
            mbox.showerror("Ошибка", "Укажите название пункта")
        elif required_point not in sum(self.points, []):
            mbox.showinfo("Нет маршрута", "Через данный пункт не проходит ни один маршрут")
        else:
            tk.Label(window, text='Проходят маршруты:').grid(row=2, column=0, columnspan=2, sticky='W', padx=10)
            row_index = 3
            i = 0
            for pair_points, route_name in zip(self.points, self.rout_names):
                if required_point in pair_points:
                    this_rout = tk.Label(window, text=' ,'[i%2] + route_name)
                    this_rout.grid(row=row_index, column=i%2, padx=10, sticky='W')
                    if i%2 == 1:
                        row_index += 1
                    i += 1
   
    def new_file(self):
        # Создание дочернего окна
        self.new_file = tk.Toplevel(master=window)
        self.new_file.resizable(width=False, height=False)
        self.new_file.title('Создать файл')
        self.new_file.grab_set()
        # создание рамки, где будут распологать поля ввода
        frame = tk.Frame(self.new_file)
        tk.Label(frame, text='начало').grid(row=0, column=1, padx=3)
        tk.Label(frame, text='конец').grid(row=0, column=2, padx=3)
        tk.Label(frame, text='номер').grid(row=0, column=3, padx=3)
        # табуляция всех строк
        tabs = [tk.Label(frame, text=f'{i}') for i in range(1, 9)]
        # создание всех полей ввода начального пункта
        self.start_wid = [tk.Entry(frame) for _ in range(1, 9)]
        # создание всех полей ввода конечного пункта
        self.finish_wid = [tk.Entry(frame) for _ in range(1, 9)]
        # создание всех полей ввода номера маршрута
        self.number_wid = [tk.Entry(frame, width=10) for _ in range(1, 9)]
        # размещение Entry и их табуляции     
        for i in range(1, 9):
            tabs[i-1].grid(row=i, column=0, pady=5, padx=3)
            self.start_wid[i-1].grid(row=i, column=1, pady=5, padx=3)
            self.finish_wid[i-1].grid(row=i, column=2, pady=5, padx=3)
            self.number_wid[i-1].grid(row=i, column=3, pady=5, padx=3)
        # упаковка рамки
        frame.pack(padx=5, pady=2)
        # сохдание меню сохранения
        save = tk.Menu(self.new_file)
        self.new_file.config(menu=save)
        # кнопка сохранения
        save.add_command(label='Сохранить', command=self.save_file)

    def save_file(self):
        self.start_data = [data.get() for data in self.start_wid]
        self.finish_data = [data.get() for data in self.finish_wid]
        self.number_data = [data.get() for data in self.number_wid]

        new_file = fd.asksaveasfile(
            title="Сохранить файл",
            defaultextension=".txt",filetypes=(("Текстовый файл", "*.txt"),))
        with new_file:
            for i in range(8):
                new_file.write(f'{self.start_data[i]};{self.finish_data[i]};{self.number_data[i]}\n')
        
        self.new_file.destroy()
        self.filename =  new_file.name
        self.this_file['text'] = self.filename.split('/')[-1]


if __name__ == "__main__":
    window = tk.Tk()
    window.title('LAB 7')
    window.geometry('290x160+500+200')
    window.resizable(width=False, height=False)
    App(window)
