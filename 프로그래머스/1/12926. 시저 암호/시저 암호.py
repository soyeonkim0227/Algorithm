def solution(s, n):
    result = ''

    for alp in s:
        if alp.islower():
            num = 97 + (ord(alp)+n) % 97 % 26
            result += chr(num)
        elif alp.isupper():
            num = 65 + (ord(alp)+n) % 65 % 26
            result += chr(num)
        else:
            result += ' '
    return result
            
'''
대문자 65~90
소문자 97~122
124%97%26
97+alp%97%26
'''
            
