import math
import matplotlib.pyplot as plt
from tkinter import *
from threading import Thread
root = Tk()
root['bg'] = 'White'
root.geometry('350x450')
root.title('Рівняння переносу')
root.resizable(width=False, height=False)
label1 = Label(text="Введiть а - швидкiсть переносу, a > 0")
label1.pack()
label2 = Label(text="Введiть I - кiлькiсть крокiв по x, I > 0:")
label2.pack()
label3 = Label(text="Введiть J - кiлькiсть крокiв по y, J > 0:")
label3.pack()
pole1 = Entry(root, bg='LightGray')
pole1.place(x=0, y=100, width = 350, height=30)

pole2 = Entry(root, bg='LightGray')
pole2.place(x=0, y=150, width = 350, height=30)

pole3 = Entry(root, bg='LightGray')
pole3.place(x=0, y=200, width = 350, height=30)

def button():
    a = int(pole1.get())
    I = int(pole2.get())
    J = int(pole3.get())
    def fi(x):
     return x**3

    def psi( t):
     return t + 1

    def func( x, t,u):
     return x + t + u + 1

    U0 = []
    U = []
    x = []
    t = []
    h = 1.0 / I
    tau = 1.0 / J
    lmd = (a * tau) / h 
    x0 = 0
    t0 = 0
    for i in range(0,I+1): 
     x.append(x0+i*h)
     U0.append(fi(x[i]))
     U.append(U0[i])

     # Начальное время
    t.append(t0)

     # Создание фигуры
    plt.ion()

    for k in range(1,J+1):
        # Граничное условие
     U[0]=psi(0)

    # Заполнение массива времени
     t.append(t0+k*tau)

    # Цикл по координате
     for i in range(1,J):
        # Явная разностная схема
        U[i]=U0[i]+tau*(func(U0[i],x[i],t[k])-a*(U0[i]-U0[i-1])/h)
    # Переход из одного временного шага к другому
     U0=U;
     print(U)
     # Построение графика
     plt.clf()
     plt.plot (x, U)
     plt.grid()
     plt.xlim(0,3)
     plt.ylim(0,3)
     plt.xlabel('x')
     plt.ylabel('u(x)')
     plt.title('t = '+str(float("{0:.3f}".format(t[k]))))
     plt.draw()
     plt.pause(0.01)
     plt.ioff()
# Отрисовка графика
    plt.show()

    
btn = Button(root, text='result', bg='LightGrey', command=button)
btn.place(x=100, y=250,  height=100, width=75)
