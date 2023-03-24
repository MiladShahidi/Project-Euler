from scipy.linalg import null_space
import numpy as np


def contains_origin(tr):
    nullspace = null_space(tr)
    nullspace = nullspace / nullspace.sum()

    return np.all(nullspace > 0)


if __name__ == '__main__':
    positives = 0
    with open('data/p102_triangles.txt', 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            tr = np.array([int(x) for x in line.split(',')]).reshape(3, 2).transpose()
            positives += int(contains_origin(tr))

    print(positives)
