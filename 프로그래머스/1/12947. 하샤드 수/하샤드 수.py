def solution(x):
    cnt = 0
    for s in str(x):
        cnt += int(s)
    return True if x % cnt == 0 else False