import re


def add(numberStr):
    if numberStr == "":
        return 0
    else:
        numList = re.split(r'[\\n,]', numberStr)
        sumNum = 0
        for num in numList:
            if num != '':
                sumNum += int(num)
        return sumNum


if __name__ == "__main__":
    numbers = input()
    print(add(numbers))