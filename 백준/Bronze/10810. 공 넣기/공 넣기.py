n, m = map(int, input().split())
basket = [0 for _ in range(n)]

for i in range(m):
    i, j, k = map(int, input().split())
    for num in range(i, j+1):
        basket[num-1] = k
        
result = ' '.join(str(s) for s in basket)
print(result)