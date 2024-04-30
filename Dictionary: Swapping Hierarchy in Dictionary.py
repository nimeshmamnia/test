"""
Input : test_dict = {‘Gfg’: { ‘a’ : [1, 3, 7, 8], ‘b’ : [4, 9], ‘c’ : [0, 7]}} 
Output : {‘c’: {‘Gfg’: [0, 7]}, ‘b’: {‘Gfg’: [4, 9]}, ‘a’: {‘Gfg’: [1, 3, 7, 8]}}
Input : test_dict = {‘Gfg’: {‘best’ : [1, 3, 4]}} 
Output : {‘best’: {‘Gfg’: [1, 3, 4]}} 
"""

test_dict = {'Gfg': {'a': [1, 3], 'b': [3, 6], 'c': [6, 7, 8]},
             'Best': {'a': [7, 9], 'b': [5, 3, 2], 'd': [0, 1, 0]}}

res = {}

for key1, value1 in test_dict.items():
    for key2, value2 in value1.items():
        if key2 not in res:
            res[key2] = {}
        res[key2][key1] = value2

print(res)

