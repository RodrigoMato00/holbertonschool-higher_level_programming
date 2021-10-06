#!/usr/bin/python3
"""NumPy
la utilizamos para crear matrice
y realizar operaciones con las mismas
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """funcion que multiplica
    dos matrices.
    m_a: lista de lista de ins o floats
    m_b: lista de listas de ints o floats
    """
    return (np.matmul(m_a, m_b))
    """matmul: calcula el producto
       de dos matrices"""
