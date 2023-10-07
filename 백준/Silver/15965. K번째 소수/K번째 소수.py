import math

sosoo = []
num = 10 ** 7
halfNum = round(math.sqrt(num))

K = int(input())

lst = [0 for _ in range(num)]
lst[0] = lst[1] = 1

for i in range(2, halfNum):
    if lst[i] == 0:
        for j in range(i*2, num, i):
            lst[j] = 1

for n in range(len(lst)):
    if lst[n] == 0:
        sosoo.append(n)

print(sosoo[K-1])