n, k = map(int, input().split())
numArr = []

for i in range(1, n+1):
  if n % i == 0: numArr.append(i)

print(0 if len(numArr) < k else numArr[k-1])