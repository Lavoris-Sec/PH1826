def checker(customers, names):
    counter = 0
    for n in range(len(customers)):
        if customers[n] == names:
            counter += 1
    return counter


customerList = ['Bob', 'Anna', 'Joe', 'Bob', 'Nick', 'Anna']

all_positions = {}

unique_customers = set(customerList)

for name in unique_customers:
    count = checker(customerList, name)

    if count > 1:

        positions = []
        for i in range(len(customerList)):
            if customerList[i] == name:
                positions.append(i)

        discount_s = "ИМЕЕТ право на скидку"
        print(f"{name} встречается {count} раз -> {discount_s}")
        print(positions)
    else:
        continue
