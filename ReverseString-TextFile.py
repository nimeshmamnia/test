# import os
# os.chdir('C:\\Users\\savla\\PycharmProjects\\pythonProject')
#
# # open file1 in reading mode
# file1 = open('file1.txt', 'r')
#
# # open file2 in writing mode
# file2 = open('file2.txt', 'w')
#
# for char in file1.read():
#     if str(char) == '\n':
#         break
#     else:
#         file2.write(char)
# file2.close()
# file2 = open('file2.txt', 'r')
# txt = file2.read()[::-1]
# file2.close()
#
# file2 = open('file2.txt', 'w')
# file2.write(txt)
# Open the input file in read mode and output file in write mode
# input_file_path = 'file1.txt'
# output_file_path = 'file2.txt'
#
# with open(input_file_path, 'r') as input_file:
#     # Read lines from the input file, reverse each line, and write to the output file
#     with open(output_file_path, 'w') as output_file:
#         for line in input_file:
#             # Remove the newline character, reverse the line, and add a newline character
#             reversed_line = line.strip()[::-1] + '\n'
#             # Write the reversed line to the output file
#             output_file.write(reversed_line)
#
# print("Lines reversed and saved to file2.txt.")


input_file = "file1.txt"
output_file = "file3.txt"

with open(input_file, 'r') as file:
    with open(output_file, 'w') as output:
        for line in file:
            reversed_line = line.strip()[::-1] + '\n'
            output.write(reversed_line)

print("Lines are reversed, Successfully!")
