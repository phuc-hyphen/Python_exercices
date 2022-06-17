P = [1, 2, 5, 10]


def rendu(X, S):
    if X == 0:
        return S
    p = max([x for x in P if x <= X])

    return rendu(X - p, S + [p])


print(rendu(19, []))
