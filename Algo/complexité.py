def search(T, P, n, m):
    for i in range(n):
        if T[i:i + m] == P:
            return True
        return False


def KMP(T, P, F):
    n = len(T)
    m = len(P)
    i = j = 0
    while i < n:
        if T[i] == P[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            if j == 0:
                i += 1
            else:
                j = F[j]
    return False


F = [0, 0, 1, 2, 3]
P = "babab"

