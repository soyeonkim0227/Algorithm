import sys
num = int(sys.stdin.readline())

lst = []
cnt = 1

for _ in range(num):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort(key = lambda x: (x[1], x[0]))

start = lst[0][1]

for i in range(1, len(lst)):
    if lst[i][0] >= start:
        start = lst[i][1]
        cnt += 1

print(cnt)
