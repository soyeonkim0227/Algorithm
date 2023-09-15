def solution(numbers):
    object = 0
    for i in range(10):
        if i not in numbers:
            object += i
    return object