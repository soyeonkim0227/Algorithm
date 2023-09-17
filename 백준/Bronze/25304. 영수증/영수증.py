list = []
total = int(input())
num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    list.append(a * b)
print('Yes' if sum(list) == total else 'No')