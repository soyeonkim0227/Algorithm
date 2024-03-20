from collections import deque

def solution(s):
    dq = deque(s)
    cnt = 0
    result = 0

    for _ in range(len(s)):
        stack = []
        dq.append(dq.popleft())
        
        for s in dq:
            if s == '[' or s == '(' or s == '{':
                stack.append(s)
            elif s == ']' and stack and stack[-1] == '[': 
                stack.pop()
                cnt += 1
            elif s == ')' and stack and stack[-1] == '(': 
                stack.pop()
                cnt += 1
            elif s == '}' and stack and stack[-1] == '{': 
                stack.pop()
                cnt += 1
            else: # stack이 비어있을 때 )}]가 들어올 때나 stack[-1] 값과 같지 않을 때
                continue
        if cnt > 0 and len(stack) == 0: result += 1
    return result
                
                
                