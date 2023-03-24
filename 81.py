# This is a simpler solution for this simple case
# A more general alternative approach is implemented for problems 82 nad 83

import numpy as np
from functools import lru_cache


# The reason I implement this in a class has to do with the caching decorator below
# The decorator requires all parameters of the decorated function to be hashable
# And since np.array is not hashable I cannot pass the matrix to the function
# You could either make the matrix a global variable or use a class to make it accessible to the function
class Matrix:
    def __init__(self, elements):
        self.matrix = elements
        self.max_col = self.matrix.shape[1] - 1
        self.max_row = self.matrix.shape[0] - 1

    # The decorator caches return values of this function
    # The algorithm is not optimal and calculates the same cost multiple times
    # But by caching we can at least speed it up in practice
    @lru_cache(maxsize=None)
    def path_and_cost(self, curr_row, curr_col):
        if curr_col == self.max_col:
            path = 'D' * (self.max_row - curr_row)
            cost = np.sum(self.matrix[curr_row:, curr_col:])
        elif curr_row == self.max_row:
            path = 'R' * (self.max_col - curr_col)
            cost = np.sum(self.matrix[curr_row:, curr_col:])
        else:
            path_r, cost_r = self.path_and_cost(curr_row, curr_col+1)
            path_d, cost_d = self.path_and_cost(curr_row+1, curr_col)
            path = 'R' + path_r if cost_r <= cost_d else 'D' + path_d
            cost = self.matrix[curr_row, curr_col] + min(cost_r, cost_d)

        return path, cost


if __name__ == '__main__':
    test_elements = [
        131,
        673,
        234,
        103,
        18,
        201,
        96,
        342,
        965,
        150,
        630,
        803,
        746,
        422,
        111,
        537,
        699,
        497,
        121,
        956,
        805,
        732,
        524,
        37,
        331
    ]
    # elements = np.array(test_elements).reshape(5, 5)

    elements = np.genfromtxt('data/p081_matrix.txt', delimiter=',')
    matrix = Matrix(elements=elements)
    path, cost = matrix.path_and_cost(0, 0)
    print('Answer: ', cost)
