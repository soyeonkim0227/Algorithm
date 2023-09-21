import sys
num, standard = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

for i in lst:
    if i < standard:
        print(i, end=" ")