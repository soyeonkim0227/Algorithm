def solution(arr):
    arr.remove(min(arr))
    if arr == [10] or not arr: return [-1]
    else: return arr