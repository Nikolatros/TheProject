import matplotlib.pyplot as plt
import numpy as np


class Lab8:
    def __init__(self, x_start, x_finish, dx, eps):
        self.X = []
        self.Y = []
        x = x_start
        while x < x_finish:
            self.X.append(x)
            self.Y.append(self.taylor(x, eps))
            x += dx
            
    def taylor(self, x, eps):
        y = (x - 1)/(x + 1)
        y_add = y
        n = 1
        while abs(y_add) > eps:
            k = ((2*n+1)/(2*n+3))*((x-1)/(x+1))**2
            y_add *= k
            y += y_add
            n += 1
        return 2*y

    def data_plot(self):
        plt.plot(self.X, self.Y)
        

x_start = 1
x_finish = 100
dx = 1
eps = 0.01
b = 2

lab8 = Lab8(x_start, x_finish, dx, eps)
lab8.data_plot()

plt.plot(np.log(np.arange(x_start, x_finish, dx)) + b)

plt.savefig('lab8', dpi=300)