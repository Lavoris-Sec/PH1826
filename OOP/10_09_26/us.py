# def calculate(price_list, us_rate):
#     new_list = []
#     for i in price_list:
#         new_list.append(round(i * us_rate, 2))
#
#     return new_list


# pricesUSD = [100.34, 35, 67.99, 25.5]
#
# USDrate = 3.01


# print(calculate(pricesUSD, USDrate))


def decorator(discount):
    def wrapper(price_list, us_rate, func):
        rub_prices = func(price_list, us_rate)

        return [round(price * (1 - discount / 100), 2) for price in rub_prices]

    return wrapper


# def apply_discount(discount):
#     def decorator(func):
#         def wrapper(price_list, us_rate):
#             rub_prices = func(price_list, us_rate)
#
#             discounted_prices = [
#                 round(price * (1 - discount / 100), 2)
#                 for price in rub_prices
#             ]
#             return discounted_prices
#
#         return wrapper
#
#     return decorator

def calculate(price_list, us_rate):
    return [round(i * us_rate, 2) for i in price_list]


pricesUSD = [100.34, 35, 67.99, 25.5]

USDrate = 3.01

final_prices = decorator(15)(pricesUSD, USDrate, calculate)

# @decorator(discount=15)
# def calculate(price_list, us_rate):
#     return [round(i * us_rate, 2) for i in price_list]


# final_prices = calculate(pricesUSD, USDrate)

print(final_prices)
