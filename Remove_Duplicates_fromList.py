# Remove Duplicates from list

# Original List
mylist = [1, 10, 9, 5, 6, 4, 8, 3, 6, 2, 7, 9, 10, 3, 6]

# Ordering List. This might remove duplicates as well. However, we will write code to specifically remove any duplicates
print(set(mylist))

# Creating an empty list
new_list = []

# Adding items in new list from old one only if they are not present earlier
for i in mylist:
    if i not in new_list:
        new_list.append(i)

# Printing new list
print(new_list)
