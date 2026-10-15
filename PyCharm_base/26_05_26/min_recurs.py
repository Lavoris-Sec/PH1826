def find_minimum(numbers):
    if not numbers:
        return None

    min_element = numbers[0]

    for num in numbers[1:]:
        min_element = min(min_element, num)

    return min_element


def find_minimum_recursive(numbers):
    if not numbers:
        return None

    if len(numbers) == 1:
        return numbers[0]

    return min(numbers[0], find_minimum_recursive(numbers[1:]))


myNumbers = [2, 4, 1, 8, 3]
print(f"Минимальное число в предоставленном списке - {find_minimum(myNumbers)}")
print(f"Минимальное число в предоставленном списке при поиске рекурсией - {find_minimum_recursive(myNumbers)}")
