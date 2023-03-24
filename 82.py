import numpy as np
from functools import lru_cache


def get_dict_key_with_min_value(d):
    min_value = min(d.values())
    for k, v in d.items():
        if v == min_value:
            return k


# The reason I implement this in a class has to do with the caching decorator below
# The decorator requires all parameters of the decorated function to be hashable
# And since np.array is not hashable I cannot pass the matrix to the function
# You could either make the matrix a global variable or use a class to make it accessible to the function
class Matrix:
    def __init__(self, elements, valid_moves, target_row, target_col):
        self.matrix = elements
        self.max_col = self.matrix.shape[1] - 1
        self.max_row = self.matrix.shape[0] - 1
        self.valid_moves = valid_moves
        self.target_row = target_row
        self.target_col = target_col

    @staticmethod
    def __opposite_move(move):
        opposites = {
            'U': 'D',
            'D': 'U',
            'R': 'L',
            'L': 'R'
        }
        return opposites[move]

    # The decorator caches return values of this function
    # The algorithm is not optimal and calculates the same cost multiple times
    # But by caching we can at least speed it up in practice
    @lru_cache(maxsize=None)
    def path_and_cost(self, curr_row, curr_col, prev_move=None):
        # this is to avoid going back. Without this we will exceed max recursion depth and get recursion error
        banned_move = [self.__opposite_move(prev_move)] if prev_move is not None else []

        out_of_bounds = (not (0 <= curr_col <= self.max_col)) or (not (0 <= curr_row <= self.max_row))
        arrived_row = True if self.target_row is None else (curr_row == self.target_row)
        arrived_col = True if self.target_col is None else (curr_col == self.target_col)

        if out_of_bounds:
            path = ''
            cost = np.inf
        elif arrived_row and arrived_col:
            path = ''
            cost = self.matrix[curr_row, curr_col]  # reached the destination
        else:
            paths = {}
            costs = {}
            move_fns = {
                'R': lambda row, col: (row, col + 1),
                'L': lambda row, col: (row, col - 1),
                'U': lambda row, col: (row - 1, col),
                'D': lambda row, col: (row + 1, col)
            }
            for move in move_fns.keys():
                if move in banned_move or move not in self.valid_moves:
                    continue

                next_row, next_col = move_fns[move](curr_row, curr_col)
                paths[move], costs[move] = self.path_and_cost(next_row, next_col, prev_move=move)

            optimal_move = get_dict_key_with_min_value(costs)
            cost = self.matrix[curr_row, curr_col] + costs[optimal_move]
            path = optimal_move + paths[optimal_move]

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

    elements = np.genfromtxt('data/p082_matrix.txt', delimiter=',')

    matrix = Matrix(elements=elements,
                    valid_moves=['R', 'U', 'D'],
                    target_row=None,
                    target_col=elements.shape[1] - 1)

    costs = []
    for row in range(matrix.matrix.shape[0]):
        path, cost = matrix.path_and_cost(row, 0)
        costs.append(cost)

    print('Answer: ', min(costs))
