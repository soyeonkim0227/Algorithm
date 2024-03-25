def solution(s):
    half = len(s) // 2
    return s[half] if len(s) % 2 else s[half-1 : half+1]