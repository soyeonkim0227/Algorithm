n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
locker = 0

for _ in range(m):
    i, j = map(int, input().split())
    locker = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = locker

result = ' '.join(str(s) for s in basket)
print(result)