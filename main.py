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


first_string = input()
second_string = input()
x, y = solve_lin_eqs_system(first_string, second_string)
print(round(x, 3), round(y, 3))
