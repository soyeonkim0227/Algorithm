x, y, w, h = map(int, input().split())
result = 0

if w-x > h-y: result = h-y
else: result = w-x

if x > result: result = result
else: result = x

if y > result: result = result
else: result = y

print(result)