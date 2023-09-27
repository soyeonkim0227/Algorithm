temp = []

n, m = map(int, input().split())
basket = [num for num in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

result = ' '.join(str(s) for s in basket)
print(result)