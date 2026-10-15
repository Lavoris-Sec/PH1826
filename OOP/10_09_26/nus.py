pricesUSD = [100.34, 35, 67.99, 25.5]
print(pricesUSD)


def changePriceDecorator_v1(myFunction):
    print("Hello! Let's change your prices...")

    def simpleWrapper(argList, us_rate):
        print("I've got list of prices with {} elements. Function starts working...".format(len(argList)))
        # resutl = myFunction(argList)

        resutl = myFunction(argList, us_rate)

        resutlwithDisc = list(map(lambda x: round(x * (1 - 0.15), 2), resutl))

        # resutlwithDisc = list(map(lambda x: x * (1 - 0.15), resutl))
        print("Let's set a discount..")
        return resutlwithDisc

    return simpleWrapper


def toPriceNew(price_list, us_rate):
    return [round(i * us_rate, 2) for i in price_list]


pricesToBYN = changePriceDecorator_v1(toPriceNew)

print(pricesToBYN(pricesUSD, 3.2))

# print(toPriceNew(pricesUSD, 3.2))
