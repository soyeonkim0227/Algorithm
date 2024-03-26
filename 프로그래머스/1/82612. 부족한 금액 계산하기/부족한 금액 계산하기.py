def solution(price, money, count):
    consum = sum([price*i for i in range(1, count+1)])
    return consum - money if consum > money else 0

    # 3,6,9,12 => 30 - 20 = 10
    # 3*1
    # 3*2
    # 3*3
    # 3*4