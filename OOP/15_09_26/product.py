class Product:
    def __init__(self, name, price, discount=.0):
        self.name = name
        self.price = price
        self.set_discount(discount)

    def showInfo(self):
        return f"{self.name} стоит {round(self.price * (1 - self._discount))} BYN"

    def toUSD(self, usd_course):
        discounted_price = self.price * (1 - self._discount)
        usd = round(discounted_price / usd_course, 2)
        return usd

    def get_discount(self):
        return self._discount

    def set_discount(self, new_discount):
        if isinstance(new_discount, int):
            new_discount = round(new_discount / 100, 2)
            print("it be int")

        self._discount = float(new_discount)

        # inusd
        # showinfo


# item1 = Product("Lipton Peach Iced", 42, 0.3)
# item2 = Product("Pure Apple Juice", 28)
# print(item1.showInfo())
# print(f"Price in USD$: {item1.toUSD(3.0)}")
# print(item2.showInfo())
# print(f"Price in USD$: {item2.toUSD(3.0)}")
#
# item1.discount = 0.5
# print(f"New discount for {item1.name} - {item1.discount * 100}%.")
# print(item1.showInfo())

item1 = Product("Lipton Peach Iced", 42, 0.3)
item2 = Product("Pure Apple Juice", 28, 20)
print(item1.showInfo())
print(f"Price in USD$:{item1.toUSD(3.0)}")
print(item2.showInfo())
print(f"Price in USD$:{item2.toUSD(3.0)}")
print(item1.showInfo())
item1.set_discount(0.5)
print(f"New discount for {item1.name} - {item1.get_discount() * 100} %.")
print(item1.showInfo())
