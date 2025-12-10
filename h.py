# Author: Kuzlyaev Nikita
# https://github.com/NikitaKuzlyaev


a = str(input())
b = str(input())
c = str(input())

ok = False

# hi here!

for db in range(10):
    b = b[1:8] + b[0]


    for dc in range(10):
        c = c[1:8] + c[0]

        for i in range(8):
            if a[i] == '0' and b[i] == '0' and c[i] == '0':
                break
        else:
            ok = True

if ok:
    print("Yes")
else:
    print("No")

