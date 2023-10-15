import sys

arr = [int(input()) for _ in range(9)]
arr.sort()

sum = 0

for a in range(0, 9):
    for b in range(1, 9):
        for c in range(2, 9):
            for d in range(3, 9):
                for e in range(4, 9):
                    for f in range(5, 9):
                        for g in range(6, 9):
                            sum = a + b + c + d + e + f + g
                            if arr[a] + arr[b] + arr[c] + arr[d] + arr[e] + arr[f] + arr[g] == 100: 
                                print(arr[a], arr[b], arr[c], arr[d], arr[e], arr[f], arr[g])
                                sys.exit()