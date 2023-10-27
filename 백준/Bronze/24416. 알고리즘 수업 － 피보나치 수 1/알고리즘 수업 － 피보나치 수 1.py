n = int(input())
f1, cnt2 = 0, 0
f = [0] * (n+1)

def fib(n):
    global f1
    
    if n == 1 or n == 2:
        f1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(num):
    global cnt2
    f[1] = 1
    f[2] = 1

    for i in range(3, num+1):
        f[i] = f[i-1] + f[i-2]
        cnt2 += 1

    return f[num]

fib(n)
fib2(n)

print(f1, cnt2)