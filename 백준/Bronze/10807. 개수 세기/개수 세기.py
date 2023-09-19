import sys

num = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
search = int(sys.stdin.readline())
cnt = 0

for i in range(num):
    if data[i] == search:
        cnt += 1
print(cnt)