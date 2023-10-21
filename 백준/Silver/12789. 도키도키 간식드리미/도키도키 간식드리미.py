N = int(input())

inp = list(map(int, input().split()))

dft = 1
stack = []

while inp:
    if inp[0] == dft:
        inp.pop(0)
        dft += 1
    else: stack.append(inp.pop(0))

    while stack:
        if stack[-1] == dft:
            stack.pop()
            dft += 1
        else: break

print('Nice' if not stack else 'Sad')