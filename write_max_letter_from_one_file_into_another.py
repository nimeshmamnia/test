# file_name = input("Enter file location: ")
# file_handler = open(file_name)
# all_words = []
# for lines in file_handler:
#     lines = lines.strip()
#     words = lines.split()
#     for word in words:
#         if word not in all_words:
#             all_words.append(word)
#             max_length = len(word)
#
# for word in all_words:
#    if len(word) >= max_length:
#       max_word = word
#       max_length = len(word)
#
# print(max_word)
#
# output_file = 'test1.txt'
#
#
# #with open(file_name, 'r') as file_handler:
# with open(output_file, 'w') as output:
#         output.write(max_word)
#
# file_handler.close()
# output.close()

filename = "Nimesh_Mamnia.doc"
unique_words = []
with open(filename, 'r') as input_file:
    for lines in input_file:
        lines = lines.strip()
        words = lines.split()
        print(words)
        # for word in words:
        #     if word not in unique_words:
        #         unique_words.append(word)


# max = 0
# for word in unique_words:
#     if len(word) > max:
#         max = len(word)
#
# print(max)