def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

def LCM(x, y):
    return x*y // GCD(x, y)

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(LCM(A, B))