sosu = []
mul = 1

test = int(input())
element = list(map(int, input().split()))
element = list(set(element))

lst = [0 for _ in range(1000000)]
lst[0] = lst[1] = 1

for i in range(2, 1000):
    if lst[i] == 0:
        for j in range(i*2, 1000000, i):
            lst[j] = 1

for i in element:
    # 입력받은 원소를 리스트의 인덱스로 바꿔서 0이면 소수
    if lst[i] == 0:
        mul *= i

if mul == 1: print(-1)
else: print(mul)