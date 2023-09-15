def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else: # )
            if not stack: return False # 스택에 아무것도 없으면 F
            if '(' in stack:
                stack.pop()
                
    if not stack:
        return True
    else:
        return False