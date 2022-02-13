import re


def add(numberStr):
    sumNum = 0

    if numberStr == "":
        return sumNum
    else:
        if re.match(r'^//', numberStr):
            charList = re.split(r'\\n', numberStr)
            if len(charList) > 0:
                delimiter = charList[0][-1]
                numList = re.split(delimiter, charList[1])
                sumNum = sum_calculator(numList)

        else:
            numList = re.split(r'[\\n,]', numberStr)
            sumNum = sum_calculator(numList)

        return sumNum


def sum_calculator(numberList):
    resultSum = 0
    negFlag = False
    negList = []
    for num in numberList:
        if num != '' and int(num) > 0:
            resultSum += int(num)
        elif num == '':
            continue
        elif int(num) < 0:
            negList.append(int(num))
            negFlag = True

    if negFlag is True:
        raise ValueError("negatives not allowed " + str(negList))
    else:
        return resultSum


if __name__ == "__main__":
    numbers = input()
    print(add(numbers))
