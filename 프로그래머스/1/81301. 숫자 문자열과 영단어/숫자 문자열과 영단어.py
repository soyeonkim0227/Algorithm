def solution(s):
    numLst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    alp = ''
    result = ''
    
    for i in s:
        if i.isalpha():
            alp += i
            if alp in numLst:
                result += str(numLst.index(alp))
                alp = ''
        else:
            result += i
    return int(result)

# 알파벳이 나온다?
# alp 문자열에 추가하기 전에 배열에 기존 alp 문자열이 해당되는지 확인
# 있다면 인덱스 찾기, result에 인덱스 번호를 문자로 변환 후 삽입, alp를 빈 문자열로 변경
# 없다면 alp 문자열에 추가