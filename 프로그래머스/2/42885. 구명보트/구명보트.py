from collections import deque

def solution(people, limit):
    cnt = 0
    deq = deque(sorted(people))
    
    while deq:
        if len(deq) == 1:
            return cnt + 1
        if deq[0] + deq[-1] <= limit:
            deq.popleft()
            deq.pop()
        else:
            deq.pop()
        cnt += 1
    return cnt