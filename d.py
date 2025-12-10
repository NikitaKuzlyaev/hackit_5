# Author: Mikhailov Gleb
# https://github.com/flexyw1be


import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A, B, C = map(int, data[:3])

    if B <= 0:
        print(0)
        return

    if A >= B:
        print(1)
        return

    if A <= C:
        print(-1)
        return

    num = B - C
    d = A - C

    if num <= 0:
        k = 1
    else:
        k = (num+ d - 1) // d

    if k < 1:
        k = 1

    print(k)

if __name__ == "__main__":
    main()

