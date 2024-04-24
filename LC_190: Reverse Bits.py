def reverseBits(n):
    str_s = bin(n)
    str_s = str_s[2:]
    str_s = str_s[::-1] + ("0" * (32 - len(str_s)))
    return int(str_s, 2)


number = 10100101000001111010011100
print(reverseBits(number))

'''
Explanation: 
SOME PYTHON FUNCTIONS

bin(n) -> Converts a decimal to binary, Result is returned as a string with 0b as a prefix.
EG-> bin(7) -> "0b111"

s=s[i:] ->String slicing -> It return the substring starting from index i.
EG-> s="0b111" -> s[2:] = "111"

s=s[::-1] ->String slicing -> With no two initial arguments, it reverses the string.
EG -> s="0101", s[::-1]="1010"

int(s,2)->converts a binary string to a decimal number.
EG-> int("101",2) = 5
'''
