import math

def solution(n):
    matchedNum = int(math.sqrt(n))
    return (matchedNum+1)**2 if matchedNum**2 == n else -1