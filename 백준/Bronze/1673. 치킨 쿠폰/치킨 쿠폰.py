while True:
    try:
        coupon, stamp = map(int, input().split())
        sum = coupon

        while True:
            if coupon < stamp: break
            else: 
                sum += coupon // stamp
                coupon = coupon // stamp + coupon % stamp
        
        print(sum)

    except:
        break