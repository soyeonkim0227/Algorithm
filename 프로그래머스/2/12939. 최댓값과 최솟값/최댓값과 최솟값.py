def solution(s):
    s = list(map(int, s.split()))
    result = f'{min(s)} {max(s)}'
    return result