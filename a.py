# Author: Mikhailov Gleb
# https://github.com/flexyw1be

def solve():
    import sys

    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))

    freq = {}

    for x in a:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    cubes = 0
    for length in freq:
        cubes += freq[length] // 12

    print(cubes)


solve()

