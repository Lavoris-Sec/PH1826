numbersList1 = [10, 20, 30]
numbersList2 = [1, 2, 3]

final = list(map(lambda x, y: x ** y, numbersList1, numbersList2))

print(final)