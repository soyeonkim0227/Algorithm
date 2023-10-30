while True:
    try: 
        n = int(input())
        if n == 0: break

        new = n
        new = list(str(new))

        n = list(str(n))
        n.reverse()
        
        new = ''.join(new)
        n = ''.join(n)
        print('yes') if new == n else print('no')

    except:
        break