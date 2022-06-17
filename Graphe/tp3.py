from copy import deepcopy

from numpy import zeros
import math
import numpy as np

from numpy.linalg import matrix_power


def create_matrix(n, edges, e_plus, e_times):
    # initialization matrix
    M = [[e_plus for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] = e_times
    for i, j, w in edges:
        M[i][j] = w
    # print(M)
    return M


def floyd_warshall(n, edges, op_plus, e_plus, op_times, e_times):
    M = create_matrix(n, edges, e_plus, e_times)

    for k in range(n):
        for j in range(n):
            for i in range(n):
                M[i][j] = op_plus(M[i][j], op_times(M[i][k], M[k][j]))
    return M


def create_matrix_2(n, edges, e_plus, e_times, op_plus):
    # initialization matrix
    M = [[e_plus for _ in range(n)] for _ in range(n)]
    P = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] = e_times
    for i in range(n):
        for j in range(n):
            if M[i][j] != e_plus:
                P[i][j] = j
    for i, j, w in edges:
        Mij = M[i][j]
        M[i][j] = op_plus(w, M[i][j])
        if Mij != M[i][j]:
            P[i][j] = j
    # print(M)
    return M, P


def floyd_warshall_1(n, edges, plus, e_plus, times, e_times):
    M, P = create_matrix_2(n, edges, e_plus, e_times, plus)
    # print(np.array(P))
    for k in range(n):
        for j in range(n):
            for i in range(n):
                Mij = M[i][j]
                M[i][j] = plus(M[i][j], times(M[i][k], M[k][j]))
                if Mij != M[i][j]:
                    P[i][j] = P[i][k]
    # P[i][j] = P[j][k]
    # print(np.array(P))
    return M, P


def path(D, source, destination):
    assert (len(D) == len(D[0]))
    assert ((0 <= source < len(D)) and (0 <= source < len(D)))

    if D[source][destination] is None:
        return []
    path = [source]
    while source != destination:
        source = D[source][destination]
        if source in path or source is None:
            return []
        path.append(source)
    return path


# Compute the shortest path (as a list of vertices)
# from source to destination
# return path as a list

def op_min(a, b):
    return min(a, b)


def op_add(a, b):
    return a + b


n = 5
edges = [(0, 1, 1), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, -1), (3, 4, 2)]
edges0 = [(0, 1, 6), (0, 2, 1), (2, 3, 6), (1, 3, 2), (2, 1, 3), (3, 0, 4)]
edges1 = [(3, 8, -2), (2, 5, 4), (1, 0, 8), (5, 0, -1), (1, 7, 9), (2, 0, 11), (5, 3, 3), (8, 0, 5), (9, 7, 5),
          (2, 7, -1), (8, 2, 12), (3, 1, 4), (1, 2, -2)]
M, P = floyd_warshall_1(n, edges, op_min, math.inf, op_add, 0)
# print(path(P, 0, 3))
M, P = floyd_warshall2(n, edges, op_min, math.inf, op_add, 0)
# print(path(P, 0, 3))

# print(np.array(M))
# print(np.array(P))

# print(M)
# print(evaluate_path_pa1(n,edges,op_min, math.inf, op_add, 0, floyd_warshall, path))


#
# n = 5
# edges = [(0, 1, 1), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, -1), (3, 4, 2)]
# floyd_warshall(n, edges, op_min, math.inf, op_add, 0)
