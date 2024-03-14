from collections import deque

n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
result = []

while n > 0:
  for _ in range(k-1):
    tmp = dq.popleft()
    dq.append(tmp)
  result.append(dq.popleft())
  n -= 1

print('<' + ', '.join(str(i) for i in result) + '>')