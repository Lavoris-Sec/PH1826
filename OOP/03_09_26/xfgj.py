class myClass1:
    def sayHi(self):
        print("Hi from Class1")


class myClass2(myClass1):
    def sayHi(self):
        print("Hi from Class2")


class myClass3(myClass1):
    def sayHi(self):
        print("Hi from Class3")


class myClass4(myClass2, myClass3):
    pass


class Class1:
    def __new__(cls):
        print("Hi! I am new magic method.")
        return super(Class1, cls).__new__(cls)

    def __init__(self):
        print("Hi! I am init magic method.")


obj1 = Class1()

# myObj = myClass4()
# myObj.sayHi()
# print(myClass4.mro)
