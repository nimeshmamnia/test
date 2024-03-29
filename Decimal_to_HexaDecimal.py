def decimaltohexa(decimal):
    hexa_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if decimal == 0:
        return "0"
    else:
        remainder = decimal % 16
        return decimaltohexa(decimal // 16) + hexa_map.get(remainder, str(remainder))

decimal = int(input("Enter decimal number: "))
hexa = decimaltohexa(decimal)
print("Corresponding HexaDecimal number of", decimal, " is: ", hexa)

