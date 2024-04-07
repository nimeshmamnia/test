# -------------------Josephus problem to find the surviving person-------------
# def solve(my_list, index, k):
#     """
#     Simulates the Josephus problem to find the surviving person.
#
#     Args:
#         my_list (list): The list representing people in the circle.
#         index (int): The starting index of the person counting.
#         k (int): The number of positions to move before removing a person.
#
#     Returns:
#         int: The index of the surviving person.
#     """
#
#     if len(my_list) == 1:
#         return my_list[0]  # Return the value directly
#
#     index = (index + k - 1) % len(my_list)  # Adjust for zero-based indexing
#     removed_value = my_list.pop(index)  # Use pop to remove and return value
#     return solve(my_list, index, k)  # Recursive call with updated list
#
#
# n = int(input("Enter n: "))
# k = int(input("Enter k: "))
# index = 0  # No need to decrement k here
# my_list = list(range(1, n + 1))  # More succinct list creation
#
# ans = solve(my_list, index, k)
# print("Person survived is:", ans)
