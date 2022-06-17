def is_connected(n, edges):
    if n == 0:
        return True
    # Convert to adjacency list
    succ = [[] for a in range(n)]
    for (a, b) in edges:
        succ[a].append(b)
        succ[b].append(a)
    # DFS over the graph
    touched = [False] * n
    touched[0] = True
    todo = [0]
    while todo:
        s = todo.pop()
        for d in succ[s]:
            if not touched[d]:
                touched[d] = True
                todo.append(d)
    return sum(touched) == n


def isola_vertices(n, edges):
    isola = []
    not_isola = []
    for i in range(n):
        for (x, y) in edges:
            if i == x or i == y:
                not_isola.append(i)
        if i not in not_isola:
            isola.append(i)
    return len(isola) > 0


def odd_vertices(n, edges):
    deg = [0] * n
    for (a, b) in edges:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(n) if deg[a] % 2]


# Write a function that decides if a graph is Eulerian. return True if the graph contains a Eulerian cycle (i.e., 
# a cycle that visit each edge exactly once), and False otherwise. Note that a graph with no edge is Eulerian (an 
# empty cycle will visit all edges). conditions suffisant : ts les arête doivent être en mêm composant +   nombre de 
# sommet defré impair est soit 0 ou 2 
def is_eulerian(n, edges):
    if n > 0 and len(edges) == 0:
        return True
    if n < 0 or (not is_connected(n, edges) and not isola_vertices(n, edges)):
        return False
    deg = [0] * n
    for (a, b) in edges:
        deg[a] += 1
        deg[b] += 1
    odd_degrees = [a for a in range(n) if deg[a] % 2]
    return len(odd_degrees) == 0 or len(odd_degrees) == 2


# print(is_eulerian(5, [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (3, 1), (4, 1), (3, 2), (2, 4), (4, 3)]))  # true
# Königsberg 7 bridges
# print(is_eulerian(4, [(0, 2), (1, 0), (2, 1)]))  # False
# print((is_eulerian(4, [])))  # True
# print((is_eulerian(4, [(0, 2), (2, 3), (3, 0), (2, 0), (2, 1), (3, 1), (1, 2), (3, 2), (0, 1), (0, 0)])))  # True

#
def is_eulerian_cycle(m, edges, cycle):
    if not is_eulerian(m, edges):
        print("not eulerien")
        return False
    cur_edges = edges.copy()
    for v in range(len(cycle)):
        v_src = cycle[v]
        if v + 1 < len(cycle):
            v_dst = cycle[v + 1]
        else:
            v_dst = cycle[0]
        if (v_src, v_dst) not in cur_edges:
            if (v_dst, v_src) not in cur_edges:
                return False
            v_src = v_dst
            v_dst = cycle[v]
        # print(v_src, v_dst)
        cur_edges.remove((v_src, v_dst))
    return len(cur_edges) == 0


# true
# print(is_eulerian_cycle(4, [(0, 2), (2, 3), (3, 0), (2, 0), (2, 1), (3, 1), (1, 2), (3, 2), (0, 1), (0, 0)],
#                         [0, 3, 2, 0, 0, 2, 1, 2, 3, 1]))


def get_first_not_nul_vertices(m, edges):
    deg = [0] * m
    for (a, b) in edges:
        deg[a] += 1
        deg[b] += 1
    for i in range(len(deg)):
        if deg[i] != 0:
            return i
    return -1


def find_eulerian_cycle(m, edges):
    cur_edges = edges.copy()
    if len(cur_edges) == 0:
        return []
    cycle = []
    v_first = get_first_not_nul_vertices(m, cur_edges)

    def find_tour(u, tour):
        for (a, b) in cur_edges:
            if a == u:
                cur_edges.remove((a, b))
                find_tour(b, tour)
            elif b == u:
                cur_edges.remove((a, b))
                find_tour(a, tour)
        tour.insert(0, u)

    find_tour(v_first, cycle)
    cycle.pop(len(cycle) - 1)
    return cycle


# g0 = (4, [(0, 1), (1, 2), (2, 3), (3, 0)])

# print(is_eulerian_cycle(*g0, find_eulerian_cycle(*g0)))
#
# # # True
# g1 = (4, [(2, 0), (2, 1), (3, 1), (1, 2), (0, 2), (2, 3), (3, 0), (3, 2), (0, 1), (0, 0)])
# print(is_eulerian_cycle(*g1, find_eulerian_cycle(*g1)))

# True
# i and j is the minimum number of edges of paths that connect i to j.
# If i=j, their distance is 0, and
# if the two vertices are not connected, their distance should be returned as math.inf.

import math


def adjlist(n, edges, directed=False):
    lst = [[] for _ in range(n)]
    for (s, d) in edges:
        lst[s].append(d)
        if not directed:
            lst[d].append(s)
    return lst


def distance(n, edges, i, j):
    if i == j:
        return 0
    if len(edges) == 0:
        return math.inf
    vertices_neighbors = adjlist(n, edges)
    if len(vertices_neighbors[i]) == 0:
        return math.inf

    seen = [False] * n
    seen[i] = True
    todo = [i]
    v_distance = 0
    # # bfs
    while True:
        v_distance += 1
        for i in range(len(todo)):
            v = todo.pop(0)
            for v_next in vertices_neighbors[v]:
                if v_next == j:
                    return v_distance
                if not seen[v_next]:
                    seen[v_next] = True
                    todo.append(v_next)
        if len(todo) == 0:
            break
    return math.inf


# print(distance(5, [(0, 1), (1, 2), (2, 3), (3, 0), (1, 4), (4, 2)], 3, 4))


# 2

def eccentricity(n, edges, i):
    v_eccentricity = []
    for v in range(n):
        if v != i:
            v_distance = distance(n, edges, i, v)
            v_eccentricity.append(v_distance)
    return max(v_eccentricity)


print(eccentricity(5, [(0, 1), (1, 2), (2, 3), (3, 0), (1, 4), (4, 2), (0, 3)], 0))
# 2
print(eccentricity(5, [(1, 2), (0, 0), (3, 0), (1, 4), (4, 2)], 4))
# inf
