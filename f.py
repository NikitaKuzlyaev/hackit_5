# Author: Kuzlyaev Nikita
# https://github.com/NikitaKuzlyaev


import sys
import queue


def kill_yourself():
    print('stupid author', 1 / 0)
    sys.exit()


def solve():
    n, m = map(int, sys.stdin.readline().split())
    matrix = [sys.stdin.readline().strip() for _ in range(n)]

    inf = 1 << 60
    dp = [[inf for x in range(m)] for y in range(n)]
    dp[0][0] = 0

    vertical = '|'
    horizontal = '='

    q = queue.Queue()
    q.put((0, 0))

    while not q.empty():
        y, x = q.get()

        if matrix[y][x] == vertical:
            # go up
            if y > 0 and dp[y - 1][x] == inf:
                dp[y - 1][x] = dp[y][x] + 1
                q.put((y - 1, x))
            # go down
            if y < n - 1 and dp[y + 1][x] == inf:
                dp[y + 1][x] = dp[y][x] + 1
                q.put((y + 1, x))

        elif matrix[y][x] == horizontal:
            # go left
            if x > 0 and dp[y][x - 1] == inf:
                dp[y][x - 1] = dp[y][x] + 1
                q.put((y, x - 1))
            # go right
            if x < m - 1 and dp[y][x + 1] == inf:
                dp[y][x + 1] = dp[y][x] + 1
                q.put((y, x + 1))

        else:
            kill_yourself()

    if dp[n - 1][m - 1] == inf:
        print(-1)
    else:
        print(dp[n - 1][m - 1])


if __name__ == '__main__':
    solve()

