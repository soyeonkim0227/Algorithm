import sys

N = int(sys.stdin.readline())

string = [sys.stdin.readline().strip() for _ in range(N)]

result = list(string[0])

for i in range(1, N):
    for j in range(len(result)):
        if result[j] == string[i][j]:
            continue
        else: result[j] = '?'

print(''.join(result))