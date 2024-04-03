def solution(array, commands):
    result = []

    for value in commands:
        newArray = array[value[0]-1 : value[1]]
        newArray.sort()
        result.append(newArray[value[2]-1])
        
    return result