import re


def add(numberStr):
    if numberStr == "":
        return 0
    else:
        sumNum = 0
        if re.match(r'^//', numberStr):
            charList = re.split(r'\\n', numberStr)
            delimiter = charList[0][-1]

            numList = re.split(delimiter, charList[1])
            sumNum = sum_calculator(numList)

        else:
            numList = re.split(r'[\\n,]', numberStr)
            sumNum = sum_calculator(numList)

        return sumNum


def sum_calculator(numberList):
    resultSum = 0
    for num in numberList:
        if num != '':
            resultSum += int(num)
    return resultSum


if __name__ == "__main__":
    numbers = input()
    print(add(numbers))