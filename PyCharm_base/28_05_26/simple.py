# def plusTen(number):
#     number += 10
#     print(number)
#
#
# myNumbers = [2, 2.5, 4.56, 23]
#
# for item in myNumbers:
#     plusTen(item)

# myNumbers = [2, 2.5, 4.56, 23]
#
# newNum = lambda x: x + 10
# for num in myNumbers:
#     print(newNum(num))
#
#
# for num in myNumbers:
#     print((lambda x: x + 10)(num))


# students = [['Bob', 70],
#             ['Jane', 80],
#             ['Andy', 50]
#             ]
# print(students)
#
# sortedSts = sorted(students, key=lambda x: x[1])
#
# print(sortedSts)


studBirthYear = [2000, 1997, 2002, 1999, 2007]

open_age = lambda x: 2026 - x

for age in studBirthYear:
    print(open_age(age))
