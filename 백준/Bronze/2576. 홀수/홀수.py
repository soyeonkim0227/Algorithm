import sys

num = [int(sys.stdin.readline()) for _ in range(7)]
odd = []

for i in num:
    if i % 2 == 1:
        odd.append(i)

if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)