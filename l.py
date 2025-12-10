# Author: Mikhailov Gleb
# https://github.com/flexyw1be


import math
import sys


def solve():
    data = sys.stdin.read().split()
    index = 0

    n = int(data[index])
    R = float(data[index + 1])
    index += 2
    points = []
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        points.append((x, y))

    if n == 0:
        print(0)
        return

    angles = []
    for x, y in points:
        rad = math.atan2(y, x)
        deg = math.degrees(rad)
        if deg < 0:
            deg += 360.0
        angles.append(deg)

    angles.sort()
    extended = angles + [a + 360.0 for a in angles]

    max_count = 1
    left = 0
    for right in range(len(extended)):
        while extended[right] - extended[left] > R + 1e-9:
            left += 1
        max_count = max(max_count, right - left + 1)
        if max_count >= n:
            break

    print(min(max_count, n))


if __name__ == "__main__":
    solve()

