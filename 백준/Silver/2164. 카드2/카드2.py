from collections import deque

n = int(input())
num = deque(list(range(1, n+1)))

while len(num) > 1:
  num.popleft()
  if len(num) == 1: break
  num.append(num.popleft())

print(num[0])