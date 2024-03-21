def solution(absolutes, signs):
    sum = 0
    
    for i in range(len(absolutes)):
        if signs[i]: # 참이라면, 양수라면
            sum += absolutes[i]
        else: # 거짓이라면, 음수라면
            sum -= absolutes[i]
    return sum