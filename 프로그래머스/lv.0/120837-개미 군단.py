def solution(hp):
    result = hp // 5 + (hp % 5 // 3)
    return result + hp % 5 % 3