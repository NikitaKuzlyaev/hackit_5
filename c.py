# Author: Kuzlyaev Nikita
# https://github.com/NikitaKuzlyaev


def solve(s: str) -> tuple[int, int]:
    if len(s) == 0:
        return 0, 1

    summ, count = solve(s[0:-1])
    summ = 10 * summ
    summ += int(s[-1]) * count

    if len(s) >= 2 and s[-1] == s[-2] == '2':
        s2, c2 = solve(s[0:-2])
        s2 = s2 * 10
        summ += 4 * c2 + s2
        count += c2

    return summ, count

s = str(input())
res = solve(s)[0]
print(res)

