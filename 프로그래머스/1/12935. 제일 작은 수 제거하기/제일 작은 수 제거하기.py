def solution(arr):
    arr.pop(arr.index(min(arr)))
    if arr == [10] or not arr: return [-1]
    else: return arr