import re


class myOperator:
    @staticmethod
    def incrementer(str):
        numbers = [float(s) for s in re.findall(r'ё', str)]
        result = []
        for number in numbers:
            result.append(number + 1)
        return result

    @staticmethod
    def decrementer(str):
        numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', str)]
        result = []
        for number in numbers:
            result.append(number - 1)
        return result


userStr = "Extract 500 , 100.45, 23.1 and 1000 from my string"
print(myOperator.incrementer(userStr))
print(myOperator.decrementer(userStr))
