def hex_to_binary(hex_string):
  """
  Converts a hexadecimal string to its binary representation using recursion.

  Args:
      hex_string (str): The hexadecimal string to convert.

  Returns:
      str: The binary representation of the hexadecimal string.
  """
  hex_map = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
             '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
             'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
  if not hex_string:
    return ""
  return hex_map[hex_string[0]] + hex_to_binary(hex_string[1:])

# Example usage

hex_representation = input("Enter HexaDecimal Number: ")
binary_representation = hex_to_binary(hex_representation)

print(hex_representation, " in binary is: ",  binary_representation)
