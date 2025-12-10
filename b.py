# Author: Kuzlyaev Nikita
# https://github.com/NikitaKuzlyaev


def gacs(arr):  # dont ask about naming
    comp = [i for i in range(len(arr))]
    size = [1 for i in range(len(arr))]

    def cap(x):
        r = []
        while x != comp[x]:
            r.append(x)
            x = comp[x]
        for i in r:
            comp[i] = x
        return x

    def unite(x, y):
        x, y = cap(x), cap(y)
        if x == y: return
        if size[x] < size[y]: x, y = y, x
        size[x] += size[y]
        comp[y] = x

    for i in range(len(arr)):
        unite(i, arr[i] - 1)

    res = []
    for i in range(len(arr)):
        if cap(i) == i:
            res.append(size[i])
    return res


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if (n + m) % 2 == 1:
        print('No')
        return

    team_size = (n + m) // 2
    s = gacs(a) + gacs(b)

    possible = {0}

    for i in s:
        new = set()

        for j in possible:
            if i + j not in possible:
                new.add(i + j)

        possible.update(new)
        if team_size in possible:
            print('Yes')
            return

    print('No')
    return


if __name__ == "__main__":
    solve()

