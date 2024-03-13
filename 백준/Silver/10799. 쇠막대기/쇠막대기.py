bracket = input()
stack = []
cnt = 0

for i in range(len(bracket)):
  if bracket[i] == '(':
    stack.append(bracket[i])
  else:
    stack.pop()
    if bracket[i-1] == '(':
      cnt += len(stack)
    else:
      cnt += 1

print(cnt)