# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# print(zip(list1, list2))
# print(type(zip(list1, list2)))
# print(set(zip(list1, list2)))

a = 2

# list1 = [1, 2, 3, 4, 5]
# print(list(zip(list1)))
# print(type(zip(list1)))

a = 3

# print(list(zip()))
# print(type(list(zip())))

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# list3 = ['!', '*', '#', '-', '+']
# print(set(zip(list1, list2, list3)))

b = 1

# def sayUserHello(user):
#     msg = "Hello, " + user
#
#     def showMsf():
#         print(msg + "! Let's start...")
#
#     showMsf()
#
#
# sayUserHello('alex')

b = 2


# def sayUserHello(user):
#     msg = "Hello, " + user
#
#     def showMsf():
#         msg = "Student"
#         print(msg + "! Let's start...")
#
#     showMsf()
#     print(msg)
#
#
# sayUserHello('alex')


# def sayUserHello(user):
#     msg = "Hello, " + user
#
#     def showMsf():
#         nonlocal msg
#         msg = "Student"
#         print(msg + "! Let's start...")
#
#     showMsf()
#     print(msg)
#
#
# sayUserHello('alex')


# def sayUserHello(user):
#     msg = "Hello, " + user
#
#     def showMsf():
#         print(msg + "! Let's start...")
#
#     return showMsf
#
#
# case1 = sayUserHello('admin')
# case1()
#
# sayUserHello('alex')


# def doExercise1(var1):
#     var2 = 5
#
#     def doExercise2(var3):
#         return var1 ** var3
#
#     return doExercise2
#
#
# case1 = doExercise1(2)
# print(case1(5))
# print(case1(10))


# def launchСounter():
#     counter = 0
#
#     def incrementCounter():
#         nonlocal counter
#         counter += 1
#         return counter
#
#     return incrementCounter
#
#
# n = launchСounter()
# for i in range(5):
#     print(n())
ф = 4

def sendMsg(userTo):
    def setMsg(msgTxt):
        def setUserFrom(userFrom):
            def setLang(lang):
                print("Dear {}, Hello from {}. Welcome to {} world! {}".format(userTo, userFrom, lang, msgTxt))

            return setLang

        return setUserFrom

    return setMsg


case1 = sendMsg('admin')('Good luck!')
case2 = sendMsg('student')('See you!')('admin')
case1('teacher')('Python')
case2('C++')
