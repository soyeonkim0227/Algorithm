import sys

N = int(sys.stdin.readline())
length = [int(sys.stdin.readline()) for _ in range(N)]
length.sort()

while len(length) >= 3:
    if length[-1] >= length[-2] + length[-3]:
        length.pop()
    else:
        print(length[-1] + length[-2] + length[-3])
        break

if len(length) < 3: print(-1)