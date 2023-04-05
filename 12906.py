def solution(arr):
    answer = []
    for i in range(0, len(arr)+1):
        if arr[i] not in arr[i-1]:
            answer.append(arr[i])
            print(answer)