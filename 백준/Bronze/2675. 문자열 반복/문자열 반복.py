lst = []
test = int(input())

for _ in range(test):
    r, s = input().split()
    r = int(r)
    lst.append([r, s])

for i in lst:
    for st in i[1]:
        print(st * i[0], end='')
    print(sep='\n')