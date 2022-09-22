# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import scipy.linalg as linalg

def solve_lin_eqs_system(first_str, second_str):
    a11, a12, b1 = first_str.split(' ')
    a21, a22, b2 = second_str.split(' ')
    index_matrix = np.array([
        [a11, a12],
        [a21, a22]
    ])
    result_vector = np.array([b1, b2])

    return linalg.solve(index_matrix, result_vector)

first_string = '1 5 11'
second_string = '2 3 8'
x, y = solve_lin_eqs_system(first_string, second_string)
print(x, y)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
