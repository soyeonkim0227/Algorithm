import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
compare = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > compare: compare = arr[i][j]

print(compare)

for i in range(9):
    for j in range(9):
        if arr[i][j] == compare:
            print(i+1, j+1)