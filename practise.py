def bits_to_bytes(bits_string):
    """
    Converts a string of bits to a bytes object.

    Args:
        bits_string (str): A string containing only '0' and '1' characters representing bits.

    Returns:
        bytes: The converted bytes object.

    Raises:
        ValueError: If the input string length is not a multiple of 8 (not a valid byte).
    """

    # Check for invalid input length (not a multiple of 8)
    if len(bits_string) % 8 != 0:
        raise ValueError("Invalid input: Bits string length must be a multiple of 8.")

    # Convert the bit string to a list of 8-bit chunks
    byte_chunks = [bits_string[i:i + 8] for i in range(0, len(bits_string), 8)]

    # Convert each 8-bit chunk to an integer (representing the byte value)
    byte_values = [int(chunk, 2) for chunk in byte_chunks]

    # Create and return the bytes object from the list of integer values
    return bytes(byte_values)


# Example usage
bits_string = "1100110010101101"
converted_bytes = bits_to_bytes(bits_string)

print(f"Bits string: {bits_string}")
print(f"Converted bytes: {converted_bytes}")
