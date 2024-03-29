def decimaltobinary(decimal):
    if decimal == 0:
        return "0"
    else:
        remainder = decimal % 2
        return decimaltobinary(decimal // 2) + str(remainder)

decimal = int(input("Enter decimal number: "))
binary = decimaltobinary(decimal)
print("Corresponding Binary number of", decimal, " is: ", binary)

