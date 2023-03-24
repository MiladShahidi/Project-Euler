import numpy as np
from functools import lru_cache


class Matrix:
    def __init__(self, elements):
        self.matrix = elements
        self.max_x = self.matrix.shape[1] - 1
        self.max_y = self.matrix.shape[0] - 1

    # The decorator caches return values of this function
    # The algorithm is not optimal and calculates the same cost multiple times
    # But by caching we can at least speed it up in practice
    @lru_cache(maxsize=None)
    def path_and_cost(self, x, y):
        print(x, y, end='\r')
        if x == self.max_x:
            path = 'D' * (self.max_y - y)
            cost = np.sum(self.matrix[y:, x:])
        elif y == self.max_y:
            path = 'R' * (self.max_x - x)
            cost = np.sum(self.matrix[y:, x:])
        else:
            path_r, cost_r = self.path_and_cost(x+1, y)
            path_d, cost_d = self.path_and_cost(x, y+1)
            path = 'R' + path_r if cost_r <= cost_d else 'D' + path_d
            cost = self.matrix[y, x] + min(cost_r, cost_d)

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
