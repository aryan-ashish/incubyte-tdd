
def add(numberStr):
    if numberStr == "":
        return 0
    else:
        numList = numberStr.split(",")
        sumNum = 0
        for num in numList:
            sumNum += int(num)
        return sumNum


if __name__ == "__main__":
    numbers = input()
    print(add(numbers))