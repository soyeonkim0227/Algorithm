def solution(name, yearning, photo):
    userDict = {}
    result = []
    
    for key, value in zip(name, yearning):
        userDict[key] = value
        
    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                sum += userDict[photo[i][j]]
        result.append(sum)
        
    return result