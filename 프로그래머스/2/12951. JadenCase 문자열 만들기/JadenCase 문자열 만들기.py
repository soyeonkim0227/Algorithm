def solution(s):
    result = ''
    # s = s.capitalize()
    # print(s)
    
    # 65 ~ 90 97~122
    for value in s:
        # 알파벳이라면?
        # result이 비어있거나 직전 문자열이 공백일 경우 대문자로 변경, 아니라면 소문자로 변경
        # 중간 글자가 이미 소문자라면?
        # 중간 글자가 대문자라면?
        if 65 <= ord(value) <= 90 or 97 <= ord(value) <= 122:
            if not result or result[-1] == ' ':
                result += (value if 65 <= ord(value) <= 90 else chr(ord(value) - 32))
            else:
                result += (value if 97 <= ord(value) <= 122 else chr(ord(value) + 32))
        # 공백이라면? 숫자라면?
        else:
            result += value
            
    return result
    
    # 처음 입력받은 공백도 결과값에 추가해줘야함.
#     answer = []
#     s = s.split(" ")
#     for value in s:
#         if value == "":
#             print(value)
#             answer.append(value)
#         elif value[0].isalpha() == False:
#             value = value.lower()
#             answer.append(value)
#         else:
#             if value == " ":
#                 answer.append(value)
#             else:
#                 value = value.lower()
#                 value = value.capitalize()
#                 answer.append(value)

#     return " ".join(answer)