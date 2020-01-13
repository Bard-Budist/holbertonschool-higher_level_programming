import numpy as np
"""
    Mul Matriz
"""
def lazy_matrix_mul(m_a, m_b):
    for i in m_a:
        if (type(i) is not integer):
            raise 
    return (np.dot(m_a, m_b))