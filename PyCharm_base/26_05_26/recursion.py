#Факториал

def f(n):
    if n == 0:
        return 1
    res = n * f(n-1)
    print(res)
    return res


print(f(0))

