'''
Write a function that takes the binary representation of a positive integer and returns the number of set bits
it has (also known as the Hamming weight).
'''


def hammingWeight(n):
    # Initialize a counter variable to 0
    count = 0
    # Loop until n is 0
    while n != 0:
        # If the last bit of n is 1, increment the counter
        if n & 1 == 1:
            count += 1
        # Shift n to the right by 1 bit
        n = n >> 1
    # Return the counter
    return count


print(hammingWeight(11))
print(hammingWeight(128))
print(hammingWeight(2147483645))
