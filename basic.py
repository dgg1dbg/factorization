def basic(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 2

    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and i != n:
            return i
            break
    else:
        return 'prime'

if __name__ == "__main__":
    n = int(input())
    print(basic(n))