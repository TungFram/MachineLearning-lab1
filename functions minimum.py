import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def f_x(x, a, b):
    return (x + a) ** 2 - b


def g_x(f):
    return np.abs(f)


print('Enter parameter a: ')
a = int(input())
print('Enter parameter b:')
b = int(input())

x_list = np.linspace(-15, 15, num=10000)
x_min = x_list[np.argmin(f_x(x_list, a, b))]
y_min = f_x(x_min, a, b)
print("Minimum of f(x) is: (" + str(x_min) + " ; " + str(y_min) + ").")

gx_min_left = x_list[np.argmin(g_x(f_x(x_list, a, b)))]
if(y_min < 0):
    new_x_list = np.linspace((gx_min_left + 0.1), 15, num=10000)
    gx_min_right = new_x_list[np.argmin(g_x(f_x(new_x_list, a, b)))]

    gy_min_left = f_x(gx_min_left, a, b)
    gy_min_right = f_x(gx_min_left, a, b)

    print("First minimum of g(x) is: (" + str(gx_min_left) + " ; " + str(gy_min_left) + ").")
    print("Second minimum of g(x) is: (" + str(gx_min_right) + " ; " + str(gy_min_right) + ").")

elif(y_min > 0):
    gx_min = x_min
    gy_min = y_min
    print("Minimum of g(x) is: (" + str(gx_min) + " ; " + str(gy_min) + ").")

print(" ")

plt.figure(num=0, dpi=350)
plt.subplot(221)
plt.plot(x_list, f_x(x_list, a, b), label="f(x)")
plt.plot(x_min, f_x(x_min, a, b), '-go', label='f(x) min')
plt.title("Function f(x)")

plt.subplot(222)
plt.plot(x_list, g_x(f_x(x_list, a, b)), label="g(x)")
plt.plot(gx_min_left, gy_min_left, '-ro')
plt.plot(gx_min_right, gy_min_right, '-ro')
plt.title("Function g(x)")


plt.show()