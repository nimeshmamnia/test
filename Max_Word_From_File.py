filename = input("Enter file Location: ")
#filehandler = open(filename)
names = {}
with open(filename, 'r', encoding='utf-8', errors='ignore') as filehandler:
    for lines in filehandler:
        lines = lines.strip()
        words = lines.split()
        for word in words:
            names[word] = names.get(word, 0) + 1

big_count = None
big_word = None
for word, count in names.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word, big_count)
filehandler.close()

