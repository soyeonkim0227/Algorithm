list = []
total = int(input())
for _ in range(total):
    n1, n2 = map(int, input().split())
    list.append([n1, n2])
list.sort()

for i in list:
    print(i[0], i[1])