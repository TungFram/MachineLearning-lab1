import numpy


def decorate_matrix(size):
    matrix = numpy.ones([size, size], dtype=int)
    matrix[1:-1:, 1:(size - 1):] = 0
    print(matrix)


matrix_size = input()
decorate_matrix(int(matrix_size))
