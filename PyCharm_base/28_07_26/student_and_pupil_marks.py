def checkStudentSuccess(name, mark):
    result = "неверный ввод"
    if 90 <= mark <= 100:
        result = "отлично"
    elif 75 <= mark < 90:
        result = "хорошо"
    elif 60 <= mark < 75:
        result = "удовлетворительно"
    elif 0 <= mark < 60:
        result = "неудовлетворительно"
    template = f"Оценка {name} - {result}"
    return template


def checkPupilSuccess(name, mark):
    result = "неверный ввод"
    if 9 <= mark <= 10:
        result = "отлично"
    elif 6 <= mark < 9:
        result = "хорошо"
    elif 3 <= mark < 6:
        result = "удовлетворительно"
    elif 0 <= mark < 3:
        result = "неудовлетворительно"
    template = f"Оценка {name} - {result}"
    return template


print(checkStudentSuccess("Jane", 78))
print(checkPupilSuccess("Bob", 6))
