def doExercise1(var1):
    def doExercise2(var2):
        return var1 ** var2

    return doExercise2


case1 = doExercise1(2)
print(case1(5))
print(case1(10))
