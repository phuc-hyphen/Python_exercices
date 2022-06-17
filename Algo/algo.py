def compute(pat):
    lastOf = {}
    lastBefore = [-1] * len(pat)
    for i in range(len(pat)):
        lastBefore[i] = lastOf.get(pat[i], -1)
        lastOf[pat[i]] = i
    print(lastBefore)
    print(lastOf)


compute("ABACA")


def max_vector(x):
    n = len(x)
    Z = [0 for i in range(n)]
    Z[0] = x[0]
    for i in range(1, n):
        Z[i] = Z[i - 1] + x[i]

    m = 0
    for i in range(n):
        for k in range(1, n - i + 1):
            m = max(m, Z[i + k - 1] - Z[i - 1])
    return m


print(max_vector([1, 2, -5, 4, 7, 2]))
