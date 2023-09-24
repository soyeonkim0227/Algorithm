namerge = []

for _ in range(10):
    num = int(input()) % 42
    if num not in namerge:
        namerge.append(num)

print(len(namerge))