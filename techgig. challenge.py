import math


def main():
    pass


def formatNumber(num):  # to remove the zeros after decimal point
    if num % 1 == 0:
        return int(num)
    else:
        return num


def initial_values(a):
    b = math.sqrt(a)
    c = a+b
    d = c/b
    return a, b, c, d


def compute():
    z = []
    j = 1
    a = int(input())
    n = int(input())
    if (a > 1) & (a > 100):
        print("Enter a number greater than 1 and less than 100")
        a = int(input())
    if (n > 1) & (n > 250):
        print("Enter a number greater than 1 and less than 250")
        n = int(input())
    for j in range(a, n+1):
        i = 1
        [a, b, c, d] = initial_values(j)
        z.extend((a, b, c, d))
        while(i < math.ceil(n/4)):
            a = c+d
            [a, b, c, d] = initial_values(a)
            # it Iterates over its argument and adding each element to the list
            z.extend((a, b, c, d))
            i = i+1
    for k in range(n):
        print(formatNumber(z[k]), end=' ')
    print()


compute()

main()
