base = [1, 1, 2, 2, 2, 8]

memory = list(map(int, input().split()))

for i in range(6):
    print(base[i]-memory[i], end=' ')