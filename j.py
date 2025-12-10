# Author: Mikhailov Gleb
# https://github.com/flexyw1be


def solve(p, b, tp, tb):
    if p == 0 and b == 0:
        return 0

    left, right = 0, p * tp + b * tb

    def can_finish(T):
        max_p1 = min(p, T // tp) if tp > 0 else p
        for p1 in range(0, max_p1 + 1):
            time1 = p1 * tp
            if time1 > T:
                break
            b1 = min(b, (T - time1) // tb) if tb > 0 else b

            p2 = p - p1
            b2 = b - b1
            if p2 < 0:
                p2 = 0
            if b2 < 0:
                b2 = 0

            if p2 * tp + b2 * tb <= T:
                return True
        return False

    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left


p, b, tp, tb = map(int, input().split())
print(solve(p, b, tp, tb))

