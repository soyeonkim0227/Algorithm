def solution(left, right):
    num = list(range(left, right+1))
    result = 0
    
    for i in num:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0: cnt += 1
        result += (-i if cnt % 2 else i)
        
    return result 