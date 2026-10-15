class UserPlayer:
    def __init__(self, name):
        self.name = name
        self.__wallet_setter = WalletFunctor()
        self.__wallet = self.__wallet_setter()

    # def updateWallet(self, new_balance):
    #     self.__wallet = new_balance
    #     print(f"Баланс игрока {self.name} успешно изменен")

    def updateWallet(self, coins):
        self.__wallet = self.__wallet_setter(coins)

    def showWallet(self):
        return f"Wallet balance player {self.name} = {self.__wallet}"


class WalletFunctor:
    def __init__(self, startCoins=100):
        self.__startCoins = startCoins

    def __call__(self, coins=0):
        self.__startCoins += coins
        txt = ""
        if self.__startCoins < 0:
            self.__startCoins -= coins
            txt = " - не изменено\nУ вас недостаточно средств"
        return f"{self.__startCoins}{txt}"


player1 = UserPlayer("Antonio")

print(player1.showWallet())

player1.updateWallet(-450)

print(player1.showWallet())


# user_wallet = WalletFunctor()
# print(f"Start state of user wallet: {user_wallet()} coins")
# print(f"State of user wallet after updating to 50 coins: {user_wallet(50)} coins")
#
# bot_wallet = WalletFunctor(50)
# print(f"Start state of bot wallet: {bot_wallet()} coins")
# print(f"State of bot wallet after updating to 20 coins: {bot_wallet(20)} coins")
