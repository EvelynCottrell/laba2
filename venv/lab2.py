from control.matlab import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *


print('0 - Иходная система')
print('1 - При Kос = Кос.пред')
print('2 - При Kос > Кос.пред')
print('3 - При Kос < Кос.пред')

func_number = int(input())

if func_number == 0:
    W1 = tf([0.6, 0], [5., 1.])
    W2 = tf([1.], [5., 1])
    W3 = tf([0.02, 1.], [0.25, 1.])
    W4 = tf([24.], [8., 1.])

elif func_number == 1:
    W1 = tf([21.78], [5., 1.])
    W2 = tf([1.], [5., 1])
    W3 = tf([0.02, 1.], [0.25, 1.])
    W4 = tf([24.], [8., 1.])
elif func_number == 2:
    W1 = tf([22.78], [5., 1.])
    W2 = tf([1.], [5., 1])
    W3 = tf([0.02, 1.], [0.25, 1.])
    W4 = tf([24.], [8., 1.])
elif func_number == 3:
    W1 = tf([14], [5., 1.])
    W2 = tf([1.], [5., 1])
    W3 = tf([0.02, 1.], [0.25, 1.])
    W4 = tf([24.], [8., 1.])
W5 = W4*W3*W2
W6 = feedback(W5, W1, sign=-1)
W0 = tf(1, 1)
W7 = W5*W1
W8 = feedback(W7, W0, sign=-1)
print(W6)
print(W1)
print(W2)
print(W3)
print(W4)

y, x = step(W6)
plt.plot(x, y, "r")
plt.title('Переходная характеристика')
plt.ylabel('Амплитуда')
plt.xlabel('Время(с)')
plt.grid(True)
plt.show()

e = np.linspace(0, 2, num=1000)
real, imag, freq = nyquist(W8, omega= e)
plt.plot()
plt.title('Диаграмма Найквиста')
plt.ylabel('+J')
plt.xlabel('+1')
plt.grid(True)
plt.show()

mag, phase, omega = bode(W6, dB=False)
plt.plot()
plt.show()

pzmap(W6)
plt.plot()
plt.grid(True)
plt.show()

D = W6.den
F = D[0]
S = F[0]
print("Коэффициенты: " + str(S))
n = len(S)
print("Количество элементов: " + str(n))
print("Полюса: " + str(pole(W6)))
w = symbols('w', real=True)
result = 0
for i in range(n):
    Z = S[i]*(I*w)**(n-1)
    result += Z
    n -= 1
print("Характеристический многочлен замкнутой системы" + str(result))
Real=re(result)
Im=im(result)
print("Действительная часть Re= " + str(Real))
print("Мнимая часть Im= " + str(Im))
x=[Real.subs({w:q}) for q in arange(0,50,0.01)]
y=[Im.subs({w:q}) for q in arange(0,50,0.01)]
plt.plot(x, y)
plt.grid(True)
plt.show()
