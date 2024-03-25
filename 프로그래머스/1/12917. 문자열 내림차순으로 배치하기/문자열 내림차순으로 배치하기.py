def solution(string):
    alp = [ord(s) for s in string]
    alp.sort(reverse=True)
    result = [chr(s) for s in alp]
    return ''.join(result)