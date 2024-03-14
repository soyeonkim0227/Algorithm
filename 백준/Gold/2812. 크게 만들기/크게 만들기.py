n, k = map(int, input().split())
numArr = list(map(int, input()))
stack = []

for i in numArr:
  while stack and k > 0 and i > stack[-1]:
    stack.pop()
    k -= 1
  stack.append(i)

if k != 0:
  stack = stack[:-k]

print(''.join(map(str, stack)))