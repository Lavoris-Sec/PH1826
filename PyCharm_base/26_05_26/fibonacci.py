# def fibonacci(n):
#     if n <= 0:
#         return 0
#
#     elif n == 1:
#         return 1
#
#     else:
#
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(6))
#
# count = int(input("Введите число"))
#
# count += 1
#
# for i in range(count):
#     print(fibonacci(i))



def fibonacci_recursive(n, a=0, b=1):

    if n < 0:
        return

    print(a)

    fibonacci_recursive(n - 1, b, a + b)


count = int(input("Введите число: "))

fibonacci_recursive(count)
