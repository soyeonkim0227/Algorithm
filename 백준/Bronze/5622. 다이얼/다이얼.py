dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0

string = input()

for i in string:
    for j in dial:
        if i in j:
            num = dial.index(j) + 3
            sum += num
print(sum)