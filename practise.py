def add_unique_chars_to_dict(s):
    char_dict = {}  # Start with an empty dictionary

    for char in s:
        if char not in char_dict:
            char_dict[char] = 1  # Add the character to the dictionary if it's not present
        else:
            char_dict[char] += 1  # Increment the count if character is already in the dictionary

    return char_dict

# Example usage
input_string = "hello world"
result_dict = add_unique_chars_to_dict(input_string)
print(result_dict)
