from operator import itemgetter

# list_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# dict_list = {'names': list_name, 'values': list_values}
# print(dict_list['values'].append(10))
# print(dict_list['values'])

# Delete anything from dictionary
rank_products = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Before Deletion", rank_products)
del rank_products['a']
print("After Deletion", rank_products)

# Add anything into dictionary
rank_products['a'] = 1
rank_products.update({'f': 6, 'g': 7})
print("After Addition", rank_products)

# Merge two dictionary in one
sales1 = {"India": 300, "China": 400}
sales2 = {"USA": 500, "Japan": 100}
# Method 1 of merging
sales = {**sales1, **sales2}
print("Sales = ", sales)
# Method 2 of merging
total_sales = sales1.copy()
total_sales.update(sales2)
print("Total Sales = ", total_sales)

# Sort Dictionary
# Sort by Key
print(sorted(sales))

# Sort by value
final_sale = {"India": 300, "Uganda": 40, 'SriLanka': 450}
print(sorted(final_sale, key=itemgetter(1)))
print(sorted(final_sale, key=itemgetter(1), reverse=True))

# Dictionary Comprehension
final_commission = {x: y * 0.10 for x, y in final_sale.items()}
print("Final Commission = ", final_commission)
simple_dict = {x: x ** 2 for x in range(1, 10)}
print("Simple Dict = ", simple_dict)
even_dict = {x: x ** 2 for x in range(1, 10) if x % 2 == 0}
print("Even Dict = ", even_dict)
odd_dict = {x: x ** 2 for x in range(1, 10) if x % 2 != 0}
print("Odd Dict = ", odd_dict)

"""# initializing dictionary
test_dict = {"Gfg": 1, "is": 3, "Best": 2}
keys = list(test_dict.keys())
values = list(test_dict.values())
print(keys + values)"""

"""test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
result = list()

for keys,values in test_dict.items():
    for items in values:
        result.append(items)

print(list(set(result)))"""

"""l1 = ['cat', 'dog', 'tac', 'god', 'act']
d1 = dict()
for items in l1:
    temp = ''.join(sorted(items))
    if temp not in d1:
        d1[temp] = []
        d1[temp].append(items)
    else:
        d1[temp].append(items)

print(d1.values())"""

"""from operator import itemgetter

test_dict = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
             'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
             'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}
result = {}
for key, value in test_dict.items():
    v1 = dict(sorted(value.items(), key=itemgetter(1)))
    result[key] = v1

res = {key: dict(sorted(val.items(), key=itemgetter(1)))
       for key, val in test_dict.items()}

print(result)
print(res)"""
