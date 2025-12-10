# Author: Kuzlyaev Nikita
# https://github.com/NikitaKuzlyaev


import sys

def solve():
    s = str(sys.stdin.readline().strip())
    k = int(sys.stdin.readline())

    f = {}
    best = 0
    l = 0
    cur = 0

    for r in range(len(s)):
        cur += 1

        if s[r] not in f:
            f[s[r]] = 1
            best = max(best, cur)
            continue

        f[s[r]] += 1

        while f[s[r]] > k:
            cur -= 1
            f[s[l]] -= 1
            l += 1

        best = max(best, cur)

    print(best)
    return


if __name__ == "__main__":
    solve()
