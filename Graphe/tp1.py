def is_simple1(n, edges):
    # checks = []
    if n > 0:
        for (x, y) in edges:
            if x < 0 or x > n - 1 or y < 0 or y > n - 1:
                return False
            # checks.append((x, y))
            if (y, x) in edges:
                return False
            if (x, x) in edges or (y, y) in edges:
                return False
        return True
    return False


# correction
def is_simple(n, edges):
    mat = [[0] * n for i in range(n)]
    for (a, b) in edges:
        if a == b or mat[a][b]:
            return False
        mat[a][b] = True
        mat[b][a] = True
    return True


def odd_vertices1(n, edges):  # impair
    odd_degree = []
    if n > 0:
        for i in range(0, n):
            degree = 0
            for (x, y) in edges:
                if x == i:
                    degree += 1
                if y == i:
                    degree += 1
            if degree == 0:
                degree += 2
            if degree % 2 != 0:
                odd_degree.append(i)
    return odd_degree.sort()


# correction
def odd_vertices(n, edges):
    deg = [0] * n
    for (a, b) in edges:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(n) if deg[a] % 2]


def is_connected1(n, edges):
    if n > 0:
        vertices_connected = dfs(n, edges, 0)
        if len(vertices_connected) == n:
            return True
        else:
            return False


def get_list_of_vertices(n, edges):
    lst = [[] for _ in range(n)]
    for (s, d) in edges:
        lst[s].append(d)
        lst[d].append(s)
    return lst


def dfs(n, edges, start):
    succ = get_list_of_vertices(n, edges)
    seen = [False] * n
    vertices = []

    def rec(s):
        seen[s] = True
        for d in succ[s]:
            if not seen[d]:
                rec(d)
        vertices.append(s)

    rec(start)
    return vertices


# print(is_simple(4, [(0, 2), (2, 3), (3, 0), (2, 0), (2, 1), (3, 1), (1, 2)]))
# print(is_simple(5, [(0, 1), (1, 2), (3, 2), (0, 3), (2, 0), (1, 3), (4, 1), (4, 2)]))

print(odd_vertices(4, [(0, 3), (3, 2), (1, 2), (3, 1)]))
print(odd_vertices(3, [(1, 1)]))
#
# print(is_connected(4, [(0, 1), (2, 1), (3, 0), (3, 1)]))
# print(is_connected(5, [(0, 1), (2, 1), (2, 0), (4, 3)]))
# print(is_connected(5, [(0, 1), (1, 3), (3, 2), (3, 4)]))


# correction
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
