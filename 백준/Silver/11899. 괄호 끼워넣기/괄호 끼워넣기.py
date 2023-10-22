bracket = input()

stack = []

for s in bracket:
    if s == ')':
        if stack and stack[-1] == '(': stack.pop()
        else: stack.append(s)
    else: stack.append(s)

print(len(stack))