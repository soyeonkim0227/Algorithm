def solution(n):
    sum = 0
    
    for i in range(1, n+1):
        divisor = n // i
        if n == i * divisor:
            sum += divisor
    return sum