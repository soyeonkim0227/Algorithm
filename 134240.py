def solution(food):
    result = ""
    
    for i in range(1, len(food)):
        result += str(i) * (food[i] // 2)
    result += str(0)
    s1 = list(result)
    s1.reverse()
    for i in range(1, len(s1)):
        result += s1[i]
    return result

