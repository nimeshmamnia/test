#my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8]
#num = 1
#for i in my_list:
#    num = num * i

# print("Multiplication of all the numbers in the list is " + str(num))

# file_name = input("Enter file name: ")
# file_handler = open(file_name)
# unique_words = []
# for line in file_handler:
#     words = line.split()
#     for word in words:
#         if word not in unique_words:
#             unique_words.append(word)

# unique_words.sort()

# print(unique_words)

file_name = input("Enter file location: ")
file_handler = open(file_name)
count = 0
all_words = []
for lines in file_handler:
    lines = lines.strip()
    words = lines.split()
    for word in words:
        if word not in all_words:
            all_words.append(word)
            max_length = len(word)


for word in all_words:
   if len(word) >= max_length:
      max_word = word
      max_length = len(word)

print(max_word)


