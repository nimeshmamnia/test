def removeknumber(nums):
    # Removing element from 3rd position
    position = 3 - 1
    start_index = 0
    length = len(nums)
    while length > 0:
        start_index = (start_index + position) % length
        print(nums.pop(start_index))
        length -= 1


# Create a list of numbers.
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
removeknumber(nums)
