import sys
lst = []

for _ in range(9):
    num = int(sys.stdin.readline())
    lst.append(num)

print(max(lst))
print(lst.index(max(lst)) + 1)