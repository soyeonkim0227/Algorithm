def solution(t, p):
    result = 0
    
    for i in range((len(t)-len(p))+1):
        if int(t[i : i+len(p)]) <= int(p):
            print(t[i : i+len(p)])
            result += 1
    return result

# 7, 0~4
# t의 길이는 12, 0~11까지만 순회하도록.
# => len(t)-len(p)