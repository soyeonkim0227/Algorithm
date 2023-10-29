money = int(input())

change = 1000 - money
sum = 0

while change != 0:
    if change - 500 >= 0: 
        change -= 500
        sum += 1
    elif change - 100 >= 0: 
        change -= 100
        sum += 1
    elif change - 50 >= 0:
        change -= 50
        sum += 1
    elif change - 10 >= 0:
        change -= 10
        sum += 1
    elif change - 5 >= 0:
        change -= 5
        sum += 1
    elif change - 1 >= 0:
        change -= 1
        sum += 1

print(sum)