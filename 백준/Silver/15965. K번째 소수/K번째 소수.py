import math
halfRange = round(math.sqrt(500000))
sosoo = []

K = int(input())

lst = [0 for _ in range(500000)]
lst[0] = lst[1] = 1

for i in range(2, halfRange):
    if lst[i] == 0:
        for j in range(i*2, 500000, i):
            lst[j] = 1

for n in range(len(lst)):
    if lst[n] == 0:
        sosoo.append(n)

print(sosoo[K-1])