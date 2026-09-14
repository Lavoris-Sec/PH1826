users = ['admin', 'teacher', 'manager']
template = "Name: {}; age: {}; scores: {}."

valid_checker = ['1', '2', '3', '4', '0']

students = [
    ['Bob', 19, 95],
    ['Fish', 25, 100],
    ['SpongeBob', 39, 20]
]
exit = 0
checck = 0

while (checck != 1):
    checkk_login = input("Введите логин - ")
    check_login = checkk_login.lower()
    if check_login in users:
        print(check_login)
        checck += 1
    else:
        print("Неверный логин!")

while (exit != 1):

    if check_login in users:
        print("1-print info")
        print("2-modify info")
        print("3-exit")

        choice = input()

        if choice == '1':
            for i in range(len(students)):
                print(f"{i + 1} - {students[i][0]}")
            id = int(input('Выберите нужного студента: '))
            id -= 1
            if check_login == users[0]:
                print(template.format(*students[id]))
            elif check_login == users[1]:
                print(f'Имя - {students[id][0]}\t Баллы - {students[id][2]}')
            elif check_login == users[2]:
                print(f'Имя - {students[id][0]}\t Возраст - {students[id][1]}')

        elif choice == '2':

            for i in range(len(students)):
                print(f"{i + 1} - {students[i][0]}")
            ids = int(input('Выберите нужного студента: '))
            ids -= 1

            sExit = 0
            while (sExit != 1):
                checker = input('Что вы хотите поменять? \n 1 - Имя \n 2 - Возраст \n 3 - Баллы \n '
                                '4 - Вывести что имеем сейчас \n 0 - Выход\n')

                if checker not in valid_checker:
                    print('Неверный ввод')

                    continue

                if checker != '0':

                    if checker == '1':
                        if check_login == 'teacher':
                            print('Нет доступа')

                            continue
                        else:
                            students[ids][0] = input('Введите новое имя: ')
                            print(f'Имя успешно изменено! {students[ids]}')

                    elif checker == '2':
                        if check_login == 'teacher':
                            print('Нет доступа')

                            continue
                        else:
                            students[ids][1] = int(input('Введите новый возраст: '))
                            print(f'Возраст успешно изменен! {students[ids]}')

                    elif checker == '3':
                        if check_login == 'manager':
                            print('Нет доступа')

                            continue
                        else:
                            students[ids][2] = int(input('Введите новую оценку: '))
                            print(f'Балл успешно изменен! {students[ids]}')

                    elif checker == '4':
                        if check_login == 'admin':
                            print(template.format(*students[ids]))
                        elif check_login == 'teacher':
                            print(f'Name: {students[ids][0]}; scores: {students[ids][2]}')
                        elif check_login == 'manager':
                            print(f'Name: {students[ids][0]}; age: {students[ids][1]}')

                elif checker == '0':
                    sExit += 1

        elif choice == '3':
            exit += 1

print('Успешный выход')
