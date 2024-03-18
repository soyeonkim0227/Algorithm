def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        sumTmp = 0
        for j in range(i, n+1):
            sumTmp += j
            if sumTmp == n: cnt += 1
            elif sumTmp > n: break
            
    return cnt
            