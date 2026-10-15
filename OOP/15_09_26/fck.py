class myDecorator:
    def __init__(self, fn):
        self.fn = fn
        self.__memory_call = []

    def showMemoryState(self):
        return f"{self.__memory_call}"
        # t = 0
        # for i in self._memory_call:
        #     print(f"{t} - {i}\n")
        #     t += 1

    def __call__(self, num1, num2):
        t = self.fn(num1, num2) ** 2
        self.__memory_call.append(t)
        return t


@myDecorator
def addNums(x, y):
    return x + y


print(addNums(2, 3))

print(addNums(3, 3))
print(addNums.showMemoryState())
print(addNums(4, 3))
print(addNums.showMemoryState())
