def solution(s):
    s = list(s)
    stack = []
    
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
    return 0 if stack else 1

'''
b와 a -> x
a와 a -> o, 둘 다 제거
bbaa

다시 처음 인덱스로 돌아와서
b와 b -> o, 둘 다 제거
aa

다시 처음 인덱스로 돌아와서
a와 a -> o, 둘 다 제거

s가 비어 있다면 1 반환, 아니라면 0 반환
'''