A, B = map(int, input().split())

sum = 0

for i in str(A):
    for j in str(B):
        sum += int(i) * int(j)

print(sum)