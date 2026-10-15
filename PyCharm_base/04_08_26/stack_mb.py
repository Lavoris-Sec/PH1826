stack_list = ["([{})][()(){}]"]

matching_brackets = {")": "(", "}": "{", "]": "["}


def validate_brackets(text_string):
    check_list = []

    for element in text_string:
        if element in matching_brackets.values():
            check_list.append(element)

        elif element in matching_brackets:
            if not check_list:
                print("Ошибка: Закрывающая скобка без открывающей!")
                return False

            last_open = check_list.pop()
            if matching_brackets[element] != last_open:
                print(f"Ошибка: Не совпали скобки! Ожидалось закрытие для '{last_open}', но пришла '{element}'")
                return False

    if len(check_list) == 0:
        print("Успех: Все скобки расставлены корректно.")
        return True
    else:
        print(f"Ошибка: Не все скобки закрылись! Осталось в стеке: {check_list}")
        return False


result = validate_brackets(stack_list[0])
print(f"Результат программы: {result}")
