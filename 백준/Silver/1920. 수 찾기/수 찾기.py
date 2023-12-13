N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()
result = [0] * M

for idx, target in enumerate(m_arr):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if n_arr[mid] < target:
            start = mid + 1
        elif n_arr[mid] > target:
            end = mid - 1
        else:
            result[idx] = 1
            break

[print(i) for i in result]