#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i =  []
    for row in matrix:
        i.append([j ** 2 for j in row])
    return i
