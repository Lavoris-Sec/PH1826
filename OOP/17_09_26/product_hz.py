# class Product:
#     def __init__(self, name, price, discountPercentage=5):
#         self.name = name
#         self.price = price
#         self.__discountPercentage = discountPercentage * 100 if 0 < discountPercentage < 1 else discountPercentage
#
#     def getDiscount(self):
#         return self.__discountPercentage
#
#     def setDiscount(self, value):
#         if 0.1 <= value <= 0.75:
#             self.__discountPercentage = value * 100
#         elif 10 <= value <= 75:
#             self.__discountPercentage = value
#         else:
#             print(f"Discount value less than 10% or greater than 75% is not possible!")
#
#     def delDiscount(self):
#         print("It is impossible to delete this property!")
#
#     def showInfo(self):
#         print(f"name:{self.name}, price with discount: {self.price * (1 - self.getDiscount() / 100)} BYN.")
#
#     def toUSD(self, usdExchRate):
#         return self.price * (1 - self.getDiscount()) / usdExchRate
#
#     discountPercentage = property(
#         fget=getDiscount,
#         fset=setDiscount,
#         fdel=delDiscount,
#         doc="Product discount property."
#     )
#
#
# item1 = Product("Lipton Peach Iced", 42, 30)
# del item1.discountPercentage
# help(Product.discountPercentage)


class Product:
    def __init__(self, name, price, discountPercentage=25):
        self.name = name
        self.price = price
        self.__discountPercentage = discountPercentage * 100 if 0 < discountPercentage < 1 else discountPercentage

    @property
    def discountPercentage(self):
        return self.__discountPercentage

    @discountPercentage.setter
    def discountPercentage(self, value):
        if 0.1 <= value <= 0.75:
            self.__discountPercentage = value * 100
        elif 10 <= value <= 75:
            self.__discountPercentage = value
        else:
            print(f"Discount value less than 10% or greater than 75% is not possible!")

    @discountPercentage.deleter
    def discountPercentage(self):
        print("It is impossible to delete this property!")

    def showInfo(self):
        print(f"name:{self.name}, price with discount: {self.price * (1 - self.__discountPercentage / 100)} byn.")

    def toUSD(self, usdExchRate):
        return self.price * (1 - self.__discountPercentage) / usdExchRate


item1 = Product("Lipton Peach Iced", 42, 30)
del item1.discountPercentage
