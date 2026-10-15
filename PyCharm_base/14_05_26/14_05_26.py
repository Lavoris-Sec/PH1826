'''
def upper(name):
    # mod_name = name.upper()
    # return mod_name
    return name.upper()

login = input('Имя')

print(upper(login))
'''

# ↓Одно задание
# def y(x, z):
#
#     if x + z <= 0:
#         return 5 * x + 2 * z
#     else:
#         return 10 * x - 3 * z
#
#     # if x + z <= 0:
#     #     result = 5 * x + 2 * z
#     # elif x + z > 0:
#     #     result = 10 * x - 3 * z
#     #
#     # return result
#
# x = int(input("X"))
# z = int(input("Z"))
#
# print(f'y = {y(x, z)}')##


# def calculate(a, b):
#     return a + b
#
# x = int(input("Введите X"))
# z = int(input("Введите Z"))
# formula=''
# if calculate(x, z) <= 0:
#     y = 5 * x + 2 * z
#     formula = '5 * x + 2 * z'
# else:
#     y = 10 * x - 3 * z
#     formula = '10 * x - 3 * z'
#
# print(f'Y = {y}, Формула - {formula}')
# ↑


def checker(customers, name):
    count = 0
    for n in range(len(customers)):
        if customers[n] == name:
            print(n)
            count += 1
    return count

customerList=['Bob', 'Anna', 'Joe', 'Bob', 'Nick']

searchName = input("Введите имя клиента")



count = checker(customerList, searchName)

haveDiscount = 'НЕ ИМЕЕТ право'

if count > 1:
    haveDiscount = 'ИМЕЕТ право '

print(f"{searchName} встречается {count} раза, на скидку {haveDiscount}")

