nums = [2, 7, 11, 15, 4, 5, -6]
target = 9
temp = {}
for indices, value in enumerate(nums):
    remaining = target - value
    if remaining not in temp:
        temp[value] = indices
    else:
        print([indices, temp[remaining]])

print(temp)
