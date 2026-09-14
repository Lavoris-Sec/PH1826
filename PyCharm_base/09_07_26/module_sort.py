myNumbers = [1.3, -2.3, -12, 11, 0.45]

sorted_numbers2 = sorted(myNumbers, key=lambda x: x ** 2)  # Или abs(x)

print(sorted_numbers2)


# myNumbers=[1.3, -2.3, -12, 11, 0.45]
# print(myNumbers)
# print(sorted(myNumbers, key=abs))
