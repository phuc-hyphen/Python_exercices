import math
import numbers
from copy import deepcopy

__all_op_templ = [["add", "0", "res = v1 + v2"],
                  ["min", "math.inf", "res = min(v1, v2)"],
                  ["max", "-math.inf", "res = max(v1, v2)"]]


class __op_count_t(object):
    def __init__(self):
        self.__counter = 0

    def reset(self):
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def __call__(self, *args, **kwargs):
        self.__counter += 1


class_template = "class __op_{0}_t(__op_count_t):\n" \
                 "  @staticmethod\n" \
                 "  def neutral():\n" \
                 "    return {1}\n" \
                 "  def __call__(self, v1, v2):\n" \
                 "    super().__call__()\n" \
                 "    {2}\n" \
                 "    return res\n"

for __a_op_templ in __all_op_templ:
    exec(class_template.format(*__a_op_templ), globals(), locals())
    exec(f"op_{__a_op_templ[0]} = __op_{__a_op_templ[0]}_t()", globals(), locals())


def __init_mat_pa_g(n, edges, op_plus, e_plus, op_times, e_times):
    # Set up the matrix
    M = [[e_plus for _ in range(n)] for _ in range(n)]
    # Matrix for the successors of each vertex
    Succ = [[None for _ in range(n)] for _ in range(n)]

    # Diag elems
    for i in range(n):
        M[i][i] = e_times
        # From a variable type point of view we should do
        # M[i][i] = op_plus(op_plus.neutral(), op_times.neutral())
        Succ[i][i] = i

    # Add the edges
    # Set of the monoid is given in w
    for (a, b, w) in edges:
        v_before = M[a][b]
        M[a][b] = op_plus(w, M[a][b])
        # From a variable type point of view we should do
        # M[a][b] = op_plus(op_plus.neutral(),
        #     op_times(op_times.neutral(), w)
        if v_before != M[a][b]:
            Succ[a][b] = b

    return M, Succ


def __init_mat_pa(n, edges, op_plus, op_times):
    return __init_mat_pa_g(n, edges, op_plus, op_plus.neutral(), op_times, op_times.neutral())


def __floyd_warshall_pa1(n, edges, op_plus, e_plus, op_times, e_times):
    # Generalised Floyd-Warshall algorithm

    M_last, _ = __init_mat_pa(n, edges, op_plus, op_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        M_current = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                M_current[i][j] = op_plus(M_last[i][j], op_times(M_last[i][k], M_last[k][j]))
        M_last = M_current

    return M_current


def __floyd_warshall_pa2(n, edges, op_plus, e_plus, op_times, e_times):
    # Generalised Floyd-Warshall algorithm
    # Inplace and transposed

    M, _ = __init_mat_pa(n, edges, op_plus, op_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        for j in range(n):
            for i in range(n):
                M[i][j] = op_plus(M[i][j], op_times(M[i][k], M[k][j]))

    return M


def __floyd_warshall_with_succ_pa1_g(n, edges, op_plus, e_plus, op_times, e_times):
    # Generalised Floyd-Warshall algorithm
    # with successor computation

    M_last, Succ = __init_mat_pa_g(n, edges, op_plus, e_plus, op_times, e_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        M_current = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                M_current[i][j] = op_plus(M_last[i][j], op_times(M_last[i][k], M_last[k][j]))
                # Check if changed
                if M_current[i][j] != M_last[i][j]:
                    Succ[i][j] = Succ[i][k]
        M_last = M_current

    return M_current, Succ


def __floyd_warshall_with_succ_pa1(n, edges, op_plus, op_times):
    return __floyd_warshall_with_succ_pa1_g(n, edges, op_plus, op_plus.neutral(),
                                            op_times, op_times.neutral())


def __floyd_warshall_with_succ_pa2_g(n, edges, op_plus, e_plus, op_times, e_times):
    # Generalised Floyd-Warshall algorithm
    # with successor computation
    # Inplace and transposed

    M, Succ = __init_mat_pa_g(n, edges, op_plus, e_plus, op_times, e_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        for j in range(n):
            for i in range(n):
                Mij = deepcopy(M[i][j])
                M[i][j] = op_plus(M[i][j], op_times(M[i][k], M[k][j]))
                # Check if changed
                if M[i][j] != Mij:
                    Succ[i][j] = Succ[i][k]

    return M, Succ


def __floyd_warshall_with_succ_pa2(n, edges, op_plus, op_times):
    return __floyd_warshall_with_succ_pa2_g(n, edges, op_plus, op_plus.neutral(),
                                            op_times, op_times.neutral())


def __path_i2j_pa1(Succ, i, j):
    assert len(Succ) == len(Succ[0])
    assert (0 <= i < len(Succ)) and (0 <= j < len(Succ))

    if Succ[i][j] is None:
        return []

    path = [i]
    while i != j:
        i = Succ[i][j]
        if (i in path) or (i is None):
            # Loop
            # Necesary for random graph generation
            return None
        path.append(i)
    return path


def __safest_path_i2j_pa(n, edges, i, j):
    M, S = __floyd_warshall_with_succ_pa1_g(n, edges, op_max, 0., op_mul, 1.)
    return __path_i2j_pa1(S, i, j)


def __rand_graph():
    # Generates a graph without "negative" loops
    import random
    random.seed()

    idem_pot_op = [op_min, op_max]
    all_op = [eval(f"op_{op}") for op, _, _ in __all_op_templ]

    while True:

        while True:
            op_plus = random.choice(idem_pot_op)
            op_times = random.choice(all_op)
            if type(op_plus) != type(op_times):
                break

        n = random.randint(10, 20)
        edges_dict = {}
        for _ in range(int(random.uniform(0.1, 0.5) * n * n)):
            while True:
                w = random.randint(-3, 15)
                if w != 0:
                    break
            while True:
                src = random.randint(0, n - 1)
                dst = random.randint(0, n - 1)
                if src != dst:
                    break

            edges_dict[(src, dst)] = w

        edges = [(a, b, w) for ((a, b), w) in edges_dict.items()]

        # Check if ok
        try:
            M1, D1 = __floyd_warshall_with_succ_pa1(n, edges, op_plus, op_times)
            M2, D2 = __floyd_warshall_with_succ_pa2(n, edges, op_plus, op_times)

            is_ok = True
            for i in range(n):
                if M1[i][i] != op_plus(op_plus.neutral(), op_times.neutral()):
                    is_ok = False
                    break
            for i in range(n):
                if not is_ok:
                    break
                for j in range(n):
                    if M1[i][j] != M2[i][j]:
                        print("Distances not equal")
                        is_ok = False
                        print_mat(M1)
                        print_mat(M2)
                        break
                    if __path_i2j_pa1(D1, i, j) is None:
                        is_ok = False
                        break
                    if __path_i2j_pa1(D2, i, j) is None:
                        is_ok = False
                        break
            if is_ok:
                return n, edges, op_plus, op_times
        except:
            pass


def __rand_graph_safety():
    # Generates a graph without "negative" loops
    import random
    random.seed()

    op_plus = op_max
    op_times = op_mul

    while True:

        n = random.randint(4, 10)
        edges = []
        for _ in range(int(random.uniform(0.2, 0.8) * n * n)):
            w = random.random()
            while True:
                src = random.randint(0, n - 1)
                dst = random.randint(0, n - 1)
                if src != dst:
                    break
            edges.append((src, dst, w))

        # Check if ok
        try:
            M1, D1 = __floyd_warshall_with_succ_pa1_g(n, edges, op_plus, 0., op_times, 1.)
            M2, D2 = __floyd_warshall_with_succ_pa2_g(n, edges, op_plus, 0., op_times, 1.)

            is_ok = True
            for i in range(n):
                if M1[i][i] != 1.:
                    is_ok = False
                    break
            for i in range(n):
                if not is_ok:
                    break
                for j in range(n):
                    if abs(M1[i][j] - M2[i][j]) > 1.e-12:
                        print("Distances not equal")
                        is_ok = False
                        print_mat(M1)
                        print_mat(M2)
                        break
                    if __path_i2j_pa1(D1, i, j) is None:
                        is_ok = False
                        break
                    if __path_i2j_pa1(D2, i, j) is None:
                        is_ok = False
                        break

            if is_ok:
                return n, edges, op_plus, op_times
        except:
            pass


def __get_edge_dict(edges):
    ed = {}
    for (a, b, w) in edges:
        ed[(a, b)] = w
    return ed


def __get_edge_dict_safety(edges):
    ed = {}
    for (a, b, w) in edges:
        ed[(a, b)] = max(w, ed.get((a, b), w))
    return ed


def __check_counters(n, edges, counters):
    return True  # Disable this check
    n_e = len(edges)
    possible_counters = []
    # Pure FW, init with neutral
    possible_counters.append((n ** 3, n ** 3))
    # Using it partially in init
    # Setting edges with plus
    possible_counters.append((n ** 3 + n_e, n ** 3))
    # Setting edges with plus and times
    possible_counters.append((n ** 3 + n_e, n ** 3 + n_e))
    # Setting diags with plus
    possible_counters.append((n ** 3 + n, n ** 3))
    # Setting edges with plus diags with plus
    possible_counters.append((n ** 3 + n_e + n, n ** 3))
    # Setting edges with plus and times diags with plus
    possible_counters.append((n ** 3 + n_e + n, n ** 3 + n_e))

    return counters in possible_counters


def evaluate_pa1(n, edges, op_plus, e_plus, op_times, e_times, fw_st):
    op_plus.reset()
    op_times.reset()

    M_pa1 = __floyd_warshall_pa1(n, edges, op_plus, e_plus, op_times, e_times)
    counters_pa1 = (op_plus.get_counter(), op_times.get_counter())

    op_plus.reset()
    op_times.reset()
    M_st = fw_st(n, edges, op_plus, e_plus, op_times, e_times)
    counters_st = (op_plus.get_counter(), op_times.get_counter())
    # COUNTER check
    # if not __check_counters(n, edges, counters_st):
    #   return False

    if (len(M_pa1) != len(M_st)) or (len(M_pa1[0]) != len(M_st[0])):
        return False

    for i in range(len(M_pa1)):
        for j in range(len(M_pa1[0])):
            if M_st[i][j] != M_pa1[i][j]:
                return False

    return True


def evaluate_random(fw_st):
    n, edges, this_plus, this_times = __rand_graph()

    return evaluate_pa1(n, edges, this_plus, this_plus.neutral(), this_times, this_times.neutral(), fw_st)


def evaluate_path_pa1(n, edges, op_plus, e_plus, op_times, e_times, fw_st, path_st):
    op_plus.reset()
    op_times.reset()

    M_pa1, D_pa1 = __floyd_warshall_with_succ_pa1_g(n, edges, op_plus, e_plus, op_times, e_times)
    assert (
        __check_counters(n, edges, (op_plus.get_counter(), op_times.get_counter()))), "Correct counter not admissible"

    op_plus.reset()
    op_times.reset()
    M_st, D_st = fw_st(n, edges, op_plus, e_plus, op_times, e_times)
    counters_st = (op_plus.get_counter(), op_times.get_counter())

    # if counters_pa1 != counters_st:
    # COUNTER check
    # if not __check_counters(n, edges, counters_st):
    #   return False

    if (len(M_pa1) != len(M_st)) or (len(M_pa1[0]) != len(M_st[0])):
        return False

    ed = __get_edge_dict(edges)
    for i in range(len(M_pa1)):
        for j in range(len(M_pa1[0])):
            # Check weight
            if M_st[i][j] != M_pa1[i][j]:
                return False
            # Check path
            ij_path_pa = tuple(__path_i2j_pa1(D_pa1, i, j))
            ij_path_st = tuple(path_st(D_st, i, j))
            if len(ij_path_st) < 2:
                if len(ij_path_st) != len(ij_path_pa):
                    return False
            else:
                w_tot = op_times.neutral()
                # Type adjust
                w_tot = op_plus(op_plus.neutral(), op_times(op_times.neutral(), w_tot))
                for (src, dst) in zip(ij_path_st[:-1], ij_path_st[1:]):
                    try:
                        w = ed[(src, dst)]
                    except KeyError:
                        # Nonexistent edge
                        return False
                    w_tot = op_plus(op_plus.neutral(), op_times(w_tot, w))
                # if w_tot != M_st[i][j]:
                if op_plus(op_plus.neutral(), op_times(op_times.neutral(), w_tot)) != \
                        op_plus(op_plus.neutral(), op_times(op_times.neutral(), M_st[i][j])):
                    return False

    return True


def evaluate_path_random(fw_st, path_st):
    n, edges, this_plus, this_times = __rand_graph()

    res = evaluate_path_pa1(n, edges, this_plus, this_plus.neutral(), this_times, this_times.neutral(), fw_st, path_st)

    return res


def evaluate_safest_path_random(path_st):
    n, edges, this_plus, this_times = __rand_graph_safety()

    M, S = __floyd_warshall_with_succ_pa1_g(n, edges, op_max, 0., op_mul, 1.)

    ed = __get_edge_dict_safety(edges)
    for i in range(n):
        for j in range(n):
            ij_path_st = path_st(n, edges, i, j)
            if len(ij_path_st) >= 2:
                w = 1
                for (src, dst) in zip(ij_path_st[:-1], ij_path_st[1:]):
                    try:
                        w *= ed[(src, dst)]
                    except KeyError:
                        return False
                if abs(w - M[i][j]) > 1e-12:
                    return False
    return True


def print_mat(M):
    n = len(M)
    assert len(M) == len(M[0]), 'Dist mat not square'
    t_str = ""
    for i in range(n):
        for j in range(n):
            s_str = str(M[i][j])
            s_str = "".join((5 - len(s_str)) * [" "]) + s_str
            t_str += s_str + ", "
        t_str += "\n"
    print(t_str)


def print_succ(S):
    n = len(S)
    assert len(S) == len(S[0]), 'Dist mat not square'
    t_str = ""
    for i in range(n):
        for j in range(n):
            if S[i][j] is not None:
                t_str += f"{S[i][j]:3d}, "
            else:
                t_str += "  N, "
        t_str += "\n"
    print(t_str)


n = 5
edges = [(0, 1, 1), (1, 0, 3), (3, 2, 1), (1, 4, 4), (4, 3, -1), (3, 4, 2)]
print(evaluate_path_pa1(n, edges, op_min, math.inf, op_add, 0, floyd_warshall, path))
print(SEPARATOR)
# Offline test min, add
offline_test = [[10,
                 [[3, 8, -2], [2, 5, 4], [1, 0, 8], [5, 0, -1], [1, 7, 9], [2, 0, 11], [5, 3, 3], [8, 0, 5], [9, 7, 5],
                  [2, 7, -1], [8, 2, 12], [3, 1, 4], [1, 2, -2]]], [12, [[1, 7, 6], [2, 4, -2], [3, 6, 4], [7, 0, -3],
                                                                         [9, 8, 15], [10, 0, 14], [2, 8, 1], [6, 0, -3],
                                                                         [4, 9, 7], [9, 3, 12], [7, 1, 10], [7, 9, 6],
                                                                         [3, 10, 4], [8, 0, 7], [8, 5, -1], [0, 5, 14],
                                                                         [11, 1, 8], [11, 10, 2], [0, 10, 1], [6, 4, 8],
                                                                         [0, 2, 3], [4, 1, 11], [3, 2, 2], [5, 1, 12],
                                                                         [2, 10, 11], [2, 9, 7]]], [15, [[9, 0, 2],
                                                                                                         [0, 12, 7],
                                                                                                         [11, 2, 7],
                                                                                                         [0, 11, 7],
                                                                                                         [8, 2, 8],
                                                                                                         [13, 3, 7],
                                                                                                         [11, 8, 15],
                                                                                                         [5, 6, -1],
                                                                                                         [0, 10, -1],
                                                                                                         [3, 11, 7],
                                                                                                         [5, 7, 13],
                                                                                                         [7, 4, 15],
                                                                                                         [4, 3, 9],
                                                                                                         [1, 6, 9],
                                                                                                         [13, 4, 15],
                                                                                                         [11, 3, 1],
                                                                                                         [12, 9, 12],
                                                                                                         [13, 0, 8],
                                                                                                         [14, 11, 11],
                                                                                                         [7, 3, 15],
                                                                                                         [13, 1, 12],
                                                                                                         [13, 14, 1],
                                                                                                         [1, 3, 6],
                                                                                                         [0, 7, 5],
                                                                                                         [4, 7, 3],
                                                                                                         [1, 10, 8],
                                                                                                         [1, 12, 3],
                                                                                                         [10, 5, 4],
                                                                                                         [12, 13, 12],
                                                                                                         [5, 8, -3],
                                                                                                         [11, 13, -1],
                                                                                                         [10, 12, -1],
                                                                                                         [11, 6, 6],
                                                                                                         [6, 0, 14],
                                                                                                         [6, 12, 6],
                                                                                                         [11, 10, 1],
                                                                                                         [2, 9, 2],
                                                                                                         [10, 9, 1],
                                                                                                         [2, 5, 5],
                                                                                                         [12, 0, 12],
                                                                                                         [3, 12, 7],
                                                                                                         [10, 11, 7],
                                                                                                         [8, 14, 3],
                                                                                                         [6, 11, 9],
                                                                                                         [4, 14, 4],
                                                                                                         [1, 4, 1],
                                                                                                         [5, 9, 8],
                                                                                                         [7, 14, 12],
                                                                                                         [6, 5, 10],
                                                                                                         [1, 5, -1],
                                                                                                         [12, 7, 14]]]]

for (n, edges) in offline_test:
    if not evaluate_path_pa1(n, edges, op_min, math.inf, op_add, 0, floyd_warshall, path):
        print(False)

# Offline test max, min
offline_test = [[16, [[0, 6, 1], [15, 11, -1], [2, 11, 2], [5, 3, 5], [11, 5, 7], [7, 9, 3], [13, 8, -3], [6, 0, 7],
                      [9, 0, -1], [14, 2, 11], [4, 5, -1], [3, 4, 6], [1, 14, 15], [3, 12, 9], [3, 6, -2], [15, 1, -1],
                      [4, 1, 2], [11, 14, 7], [8, 11, 12], [2, 15, 7], [12, 0, 7], [4, 10, 4], [2, 14, 9], [1, 4, 15],
                      [7, 4, 2], [2, 3, -2], [4, 3, 13], [14, 15, 11], [14, 13, 8], [8, 15, 8], [1, 7, 7], [10, 3, 5],
                      [14, 0, 2], [2, 1, -1], [1, 6, 12], [6, 1, 9], [8, 13, -2], [15, 2, -2], [13, 0, 2], [6, 8, 8],
                      [2, 5, 7], [10, 1, -2], [8, 5, 4], [11, 9, 5], [15, 4, -2], [0, 9, -2], [8, 14, 10], [13, 9, 9],
                      [12, 11, -1], [1, 5, 12], [1, 12, 2], [7, 15, 5], [11, 0, 14], [2, 12, 10], [13, 6, 4],
                      [13, 2, 5], [0, 7, 13], [5, 6, 13], [11, 4, 10], [13, 14, 2], [0, 4, 14], [5, 10, 5], [2, 6, 12],
                      [11, 6, 5], [15, 10, 5], [6, 3, 5], [12, 7, -1], [12, 6, 6], [8, 9, 4], [0, 3, -1], [4, 12, 9],
                      [15, 12, 1], [1, 8, 15], [12, 8, -2], [15, 5, 13], [4, 9, 6], [14, 5, 7], [11, 15, 9],
                      [12, 5, 12], [15, 7, 5], [12, 9, 4], [1, 9, -2], [9, 8, 6], [5, 12, 13], [12, 3, 12], [13, 7, 3],
                      [0, 12, 7]]], [14, [[11, 12, 4], [11, 5, 1], [11, 10, 11], [6, 13, -3], [2, 12, 10], [12, 11, 9],
                                          [11, 13, 2], [10, 3, 14], [11, 0, 13], [5, 7, 10], [8, 3, 8], [5, 10, -3],
                                          [1, 5, 9], [6, 3, 5], [6, 5, -3], [8, 4, -3], [3, 13, 2], [0, 5, 13],
                                          [9, 0, -3], [11, 8, 3], [4, 6, 11], [3, 9, 15], [1, 12, 4], [0, 12, 12],
                                          [9, 3, 5], [4, 3, 14], [12, 10, 1], [1, 4, 12], [9, 1, 14], [10, 4, 9],
                                          [12, 4, 11], [5, 11, 1], [2, 0, 8], [9, 2, 2], [6, 9, 3], [8, 12, 3],
                                          [10, 11, 5], [3, 8, 6], [2, 1, 15], [2, 5, -2], [11, 3, 8], [10, 8, 4],
                                          [10, 0, 9], [12, 7, 9], [13, 12, -1]]], [19,
                                                                                   [[3, 16, 7], [4, 14, 15], [7, 2, 13],
                                                                                    [7, 17, -3], [3, 4, 11],
                                                                                    [15, 12, 14], [18, 0, 1],
                                                                                    [16, 18, 5], [7, 1, 7], [8, 16, 11],
                                                                                    [0, 15, 8], [14, 2, 14], [5, 3, -1],
                                                                                    [5, 11, 14], [5, 15, 4], [3, 2, 6],
                                                                                    [16, 1, 11], [7, 11, 8], [2, 14, 6],
                                                                                    [0, 2, 3], [2, 13, 7], [2, 10, 1],
                                                                                    [7, 8, 14], [12, 17, 10],
                                                                                    [9, 18, 5], [17, 14, 12],
                                                                                    [2, 17, 3], [6, 15, 12],
                                                                                    [9, 12, -2], [4, 0, 7], [12, 11, 6],
                                                                                    [2, 8, 13], [17, 13, 8], [1, 6, 1],
                                                                                    [2, 3, 14], [1, 4, -1], [0, 13, 6],
                                                                                    [10, 5, 5], [18, 11, 5],
                                                                                    [11, 17, 12], [15, 8, 1], [5, 0, 8],
                                                                                    [5, 12, 8], [0, 4, 10], [6, 5, -2],
                                                                                    [0, 8, -3], [6, 8, -3],
                                                                                    [11, 10, 9]]]]

for (n, edges) in offline_test:
    if not evaluate_path_pa1(n, edges, op_max, op_max.neutral(), op_min, op_min.neutral(), floyd_warshall, path):
        print(False)

print(True)
print(SEPARATOR)
for _ in range(10):
    res = evaluate_path_random(floyd_warshall, path)
    if not res:
        print(False)
        break
if res:
    print(True)
