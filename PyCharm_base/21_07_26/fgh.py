# def simpleDecorator(myFunction):
#     print("Hello! I'm Decorator!")
#
#     def simpleWrapper():
#         print("Function starts working...")
#
#         myFunction()
#         print("See you!")
#
#     return simpleWrapper
#
#
# def simpleDecorator_v2(myFunction):
#     print("Hello! I'm Second Decorator!")
#
#     def simpleWrapper():
#         print("Let's start...")
#         myFunction()
#         print("Good luck!")
#
#     return simpleWrapper
#
#
# # @simpleDecorator
# # def sayHi():
# #     print("Welcome!")
#
# @simpleDecorator
# @simpleDecorator_v2
# def sayHi():
#     print("Welcome!")
#
#
# # sayHi()
#
#
# # def sayHi():
# #     print("Welcome!")
#
#
# def sayBye():
#     print("Bye")
#
#
# # sayHi = simpleDecorator(sayHi)
# sayHi()
#
# # sayBye = simpleDecorator(sayBye)
# # sayBye()


# def simpleDecorator_v3(myFunction):
#     print("Hello! I'm Third Decorator!")
# 
#     def simpleWrapper():
#         print("Function starts working...")
#         resutl = myFunction()
#         print("See you!")
#         return resutl
# 
#     return simpleWrapper
# 
# 
# def calculateSum():
#     print("Welcome! Let's calculate...")
#     x = int(input("x: "))
#     y = int(input("y: "))
#     return x + y
# 
# 
# calculateSum = simpleDecorator_v3(calculateSum)
# 
# total_sum = calculateSum()
# print(f"Result of calculation: {total_sum}")


def simpleDecorator_v4(myFunction):
    print("Hello! I'm Fourth Decorator!")

    def simpleWrapper(argX, argY):
        print("I've got {},{}. Function starts working...".format(argX, argY))
        result = myFunction(argX, argY)
        print("See you!")
        return result

    return simpleWrapper


def calculateSum_v1(a, b):
    print("Welcome! Let's calculate...")
    x = int(input("x: "))
    y = int(input("y: "))
    return x + y + a + b


calculateSum_v1 = simpleDecorator_v4(calculateSum_v1)

total_sum = calculateSum_v1(3, 4)
print(f"Result of calculation: {total_sum}")
