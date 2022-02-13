
def add(numberStr):
    if numberStr == "":
        return 0
    else:
        return int(numberStr)


if __name__ == "__main__":
    numbers = input()
    print(add(numbers))