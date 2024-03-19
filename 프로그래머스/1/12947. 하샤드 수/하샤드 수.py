def solution(x):
    res = 0
    for s in str(x):
        res += int(s)
    return True if x % res == 0 else False
    