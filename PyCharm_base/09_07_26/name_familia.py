user_name = input("Введите имя - ")
user_sec_name = input("Введите вашу фамилию - ")

fixed_name = lambda name, last_name: (name + ' ' + last_name).title()

fixed_name2 = lambda name, last_name: "Полное имя: {} {}".format(name, last_name).title()  # Формат в лямбде

# print(f"{fixed_name(user_name, user_sec_name)}")

print(fixed_name2(user_name, user_sec_name))
