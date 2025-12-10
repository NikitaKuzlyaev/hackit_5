# Author: Kuzlyaev Nikita
# https://github.com/NikitaKuzlyaev


x, n = map(int, input().split())
s = str(input())

a = [0, 0, 0]
a[x - 1] = 1

for _ in range(1, n + 1):
    i, j = int(s[_ - 1]) - 1, int(s[_]) - 1
    a[i], a[j] = a[j], a[i]

print(a.index(1) + 1)


