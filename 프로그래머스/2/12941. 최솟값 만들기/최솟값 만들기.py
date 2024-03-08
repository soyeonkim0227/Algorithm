def solution(A,B):
    A.sort()
    B.sort()
    
    sum = 0
    
    # while True:
    #     if cnt == len(A) + 1: break
    
    for i in range(1, len(A) + 1):
        sum += A[i-1] * B[-i]
        
    return sum