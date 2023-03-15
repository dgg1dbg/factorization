def modularofpower(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if y % 2 != 0:
            res = (res * x) % p
            y -= 1
        
        y /= 2
        x = (x * x) % p
    return res

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)