import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    inp = sys.stdin.readline().split()
    
    if inp[0] == 'push':
        elm = int(inp[1])
        stack.append(elm)

    elif inp[0] == 'pop':
        print(-1) if not stack else print(stack.pop())

    elif inp[0] == 'size':
        print(len(stack))

    elif inp[0] == 'empty':
        print(1) if not stack else print(0)

    elif inp[0] == 'top':
        print(stack[len(stack)-1]) if len(stack) != 0 else print(-1)
