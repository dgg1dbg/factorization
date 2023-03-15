from admath import modularofpower
from admath import gcd
import numpy as np


def millerrabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    i = 0
    while d % 2 != 0:
        i += 1
        d //= 2

    for i in range(k):
        if test(i, d, n) == False:
            return False
    
    return True


def test(i, d, n):
    a = np.random.randint(1, n-1)
    x = modularofpower(a, d, n)
    if x != 1 and x != n-1:
        for e in range(i):
            if x := modularofpower(x, 2, n) == n-1:
                return True
        return False
    return True

if __name__ == "__main__":
    n = int(input())
    print(millerrabin(n, 100))