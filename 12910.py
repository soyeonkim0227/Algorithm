def solution(arr, divisor):
    answer = [arr[i] for i in range(len(arr)) if arr[i] % divisor == 0]
    if not answer:
        return [-1]
            
    return sorted(answer)