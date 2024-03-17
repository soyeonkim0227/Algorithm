def solution(n):
    
    # 피보나치 수열 응용
    fb = [0 for _ in range(n+1)]
    fb[0] = 1
    fb[1] = 2
    
    if n == 1: return 1
    
    for i in range(2, n+1):
        fb[i] = (fb[i-2] + fb[i-1]) % 1234567
    print(fb)
    return fb[n-1]

# n = 1 result = 1
# n = 2 result = 2
# n = 3 result = 3
# n = 4 result = 5