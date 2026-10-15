prices_usd = [100.34, 35, 67.99, 25.5]
EXCHANGE_RATE = 90.0


def with_discount(discount_percent):
    def decorator(func):
        def wrapper(price_in_usd):
            price_in_rub = func(price_in_usd)
            final_price = price_in_rub * (1 - discount_percent / 100)
            return round(final_price, 2)

        return wrapper

    return decorator


@with_discount(15)
def to_price_new(price_in_usd):
    return price_in_usd * EXCHANGE_RATE


final_prices_rub = [to_price_new(price) for price in prices_usd]

print("Цены в рублях со скидкой:", final_prices_rub)
