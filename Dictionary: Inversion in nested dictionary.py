"""Given a nested dictionary, perform inversion of keys, i.e innermost nested becomes outermost and vice-versa.
Input : test_dict = {“a” : {“b” : {}}, “d” : {“e” : {}}, “f” : {“g” : {}}
Output : {‘b’: {‘a’: {}}, ‘e’: {‘d’: {}}, ‘g’: {‘f’: {}}
Explanation : Nested dictionaries inverted as outer dictionary keys and viz-a-vis.
Input : test_dict = {“a” : {“b” : { “c” : {}}}}
Output : {‘c’: {‘b’: {‘a’: {}}}} Explanation : Just a single key, mapping inverted till depth.
"""


def invert_dict(d):
    inverted_dict = {}
    for outer_key, inner_dict in d.items():
        for inner_key, inner_value in inner_dict.items():
            if inner_value not in inverted_dict:
                inverted_dict[inner_value] = {}
            inverted_dict[inner_value][inner_key] = outer_key
    return inverted_dict


# Test the function
test_dict = {"a": {"b": {}}, "d": {"e": {}}, "f": {"g": {}}}
inverted_dict = invert_dict(test_dict)
print(inverted_dict)
