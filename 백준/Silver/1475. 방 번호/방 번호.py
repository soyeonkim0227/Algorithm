N = input()
numArr = [int(s) for s in N]
numArr.sort()

numSet = [0 for _ in range(10)]

for i in numArr:
    if i == 6 or i == 9: 
        if numSet[5] <= numSet[8]: numSet[5] += 1
        else: numSet[8] += 1
    else: numSet[i-1] += 1

print(max(numSet))