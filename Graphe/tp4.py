from Graphe.tp4support import SA_is_augmenting_path


def is_matching(n, edges, pairs):
    seen = []
    for x, y in pairs:
        if x < 0 or x >= n or y < 0 or y >= n or x == y:
            return False
        if x in seen or y in seen:
            return False
        seen.append(x)
        seen.append(y)
    return True


def is_maximal_matching(n, edges, pairs):
    if not is_matching(n, edges, pairs):
        return False
    seen = []
    for x, y in pairs:
        seen.append(x)
        seen.append(y)
    for x, y in edges:
        if x not in seen and y not in seen:
            return False
    return True


def build_seen_v(pairs):
    seen = list()
    for x, y in pairs:
        if x not in seen:
            seen.append(x)
        if y not in seen:
            seen.append(y)
    return seen


def is_perfect_matching(n, edges, pairs):
    if not is_matching(n, edges, pairs):
        return False
    seen_match = build_seen_v(pairs)
    seen_edges = build_seen_v(edges)
    # print(seen_match)
    if len(seen_edges) != n or len(seen_match) != n:
        return False
    seen_match.sort()
    seen_edges.sort()
    return seen_match == seen_edges


def is_in(x, y, edges):
    if (x, y) in edges or (y, x) in edges:
        return True
    return False


def adjlist(n, edges, directed=False):
    lst = [[] for _ in range(n)]
    for (s, d) in edges:
        lst[s].append(d)
        if not directed:
            lst[d].append(s)
    return lst


def get_points_passed(matching):
    point_matching = []
    for x, y in matching:
        if x not in point_matching:
            point_matching.append(x)
        if y not in point_matching:
            point_matching.append(y)
    return point_matching


def find_augmenting_path(n, edges, matching):
    edges_map = adjlist(n, edges)
    matching_map = adjlist(n, matching)
    point_free = list(set(get_points_passed(edges)) - set(get_points_passed(matching)))
    if len(point_free) == 0 or (len(point_free) == 1 and len(edges_map[point_free[0]]) == 1):
        return None
    path = []
    seen = []

    def get_path(point_begin, start, match):
        path.append(start)
        if start not in seen:
            seen.append(start)
        if start == point_begin and len(path) != 1:
            return True
        if start in point_free and start != point_begin:  # if this point is a free point or point begin
            return True
        if match:  # we need a match edges
            if matching_map[start] is not None and matching_map[start][0] not in path:
                # if we have a matching edge with this point
                if not get_path(point_begin, matching_map[start][0], not match):
                    seen.remove(start)
                    path.remove(start)
                    return False
                else:
                    return True
            else:
                seen.remove(start)
                path.remove(start)
                return False
        else:  # we need a non-match edges
            for voisin in edges_map[start]:
                if voisin in point_free:  # if the voisin is a point free
                    path.append(voisin)
                    return True
                if voisin not in seen:
                    if get_path(point_begin, voisin, not match):
                        return True
            seen.remove(start)
            path.remove(start)
            return False

        # return True

    if get_path(point_free[0], point_free[0], False):
        return path
    return None


#
# def find_maximum_matching(n, edges):
#     matching = []
#
#     p = find_augmenting_path(n, edges, matching)  # This function is available.
#     matching.extend(p)
#     if p is not None:
#         return find_maximum_matching(n, edges)
#     else:
#         return matching
def vertices_to_edges(vertices: list):
    edges = []
    x = 0
    y = 1
    while y != len(vertices):
        edges.append((vertices[x], vertices[y]))
        x += 1
        y += 1
    return edges


def XOR(M, p):
    M_prim = []
    edges = vertices_to_edges(p)
    for x, y in edges:
        if (x, y) not in M and (y, x) not in M:
            M_prim.append((x, y))
    for x, y in M:
        if (x, y) not in edges and (y, x) not in edges:
            M_prim.append((x, y))
    return M_prim


def find_maximum_matching(n, edges):
    matching = []
    p = find_augmenting_path(n, edges, matching)  # This function is available.
    # update matching from p
    # matching = XOR(matching, p)
    # repeat until no more augmenting path is found
    while p is not None:
        matching = XOR(matching, p)
        p = find_augmenting_path(n, edges, matching)
    return matching


# update matching from p
# ...
# repeat until no more augmenting path is found
# ...
#     return matching

# true

# args2 = (18, [(0, 1), (1, 2), (2, 4), (2, 3), (3, 6), (4, 5), (5, 6), (6, 7),
#               (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (11, 13), (12, 14),
#               (13, 15), (14, 15), (15, 16), (16, 17)],
#          [(1, 2), (3, 6), (4, 5), (7, 8), (9, 10), (11, 13), (12, 14), (15, 16)])
# p = find_augmenting_path(*args2)
# print(SA_is_augmenting_path(*args2, p))
#
#
# matching1 = [(1, 2), (3, 4), (5, 7)]
# edges_2_3 = [(1, 2), (1, 6), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 0), (5, 7), (5, 0), (6, 7), (7, 0)]
# print(SA_is_augmenting_path(8, edges_2_3, matching1,
#                             find_augmenting_path(8, edges_2_3, matching1)))
#
# args = (6, [(0, 1), (1, 2), (0, 2), (3, 2), (3, 4), (4, 5), (5, 3)], [(2, 3), (0, 1)])
# p = find_augmenting_path(*args)
# print(SA_is_augmenting_path(*args, p))

p = find_augmenting_path(4, [(0, 1), (1, 2), (3, 2)], [(2, 1)])
# print(XOR([(2, 1)], find_augmenting_path(4, [(0, 1), (1, 2), (3, 2)], [(2, 1)])))
print(find_maximum_matching(4, [(0, 1), (1, 2), (3, 2)]))
# print(p == [0, 1, 2, 3] or p == [3, 2, 1, 0])

# true
