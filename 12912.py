def solution(a, b):
    result = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a+1):
            result += i
        return result
    else:
        for i in range(a, b+1):
            result += i
        return result