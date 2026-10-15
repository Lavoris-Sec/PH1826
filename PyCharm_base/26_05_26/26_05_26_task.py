# def is_str_palind(item):
#     word = item.lower()
#     if word == word[::-1]:
#         print("Это слово - палиндром")
#     else:
#         print("Не палиндром")
#
#
# user_input = input("Введите слово")
#
# is_str_palind(user_input)


def is_str_palindrom(item):
    if len(item) == 0:
        return True

    if item[0] != item[-1]:
        return False
    return is_str_palindrom(item[1:-1])


def mirror_is_str_palind(item):
    if len(item) == 0:
        return False

    if item[0] == item[-1]:
        return mirror_is_str_palind(item[1:-1])

    return False


user_input = input("Введите слово: ").lower()

is_str_palindrom(user_input)
mirror_is_str_palind(user_input)

if is_str_palindrom(user_input):
    print("Это слово палиндром")
else:
    print("Не палиндром")

if mirror_is_str_palind(user_input):
    print("Не палиндром - функция 2")
else:
    print("Это слово палиндром - функция 2")
