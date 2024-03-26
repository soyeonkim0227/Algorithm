def BT(v):
  if len(v) == m:
    print(' '.join(v))
    return
  for i in range(1, n+1):
    BT(v + str(i))

n, m = map(int, input().split())
BT('')