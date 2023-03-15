import numpy as np
from millerrabin import millerrabin
from admath import modularofpower
from admath import gcd


def step(t, h, c, n):
    t = (modularofpower(t, 2, n) + c) % n
    h =  (modularofpower(h, 2, n) + c) % n
    h =  (modularofpower(h, 2, n) + c) % n
    return t, h

def pollardrho(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    
    c = np.random.randint(1, n)
    t = np.random.randint(1, n)
    h = t
    d = 1
    while d == 1: 
        t, h = step(t, h, c, n)
        d = gcd(abs(t - h), n)
        if n == d:
            return pollardrho(n)
    
    return d



if __name__ == "__main__":
    n = int(input())
    if millerrabin(n, 100):
        print('n is prime!')
    else:
        print(pollardrho(n))