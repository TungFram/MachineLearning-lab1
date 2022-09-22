import numpy as np
import matplotlib.pyplot as plt


def f_x(x, a, b):
    return (x + a) ** 2 - b


def g_x(f):
    return np.abs(f)


print('Enter parameter a: ')
a = int(input())
print('Enter parameter b:')
b = int(input())

x_list = np.linspace(-15, 15, num=10000)
f_list = f_x(x_list, a, b)
g_list = g_x(f_list)

plt.plot(x_list, f_list)
plt.title("Functions")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend

