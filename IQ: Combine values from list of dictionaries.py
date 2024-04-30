def combine_dicts(dict_list1, dict_list2):
    combined_dict = {}

    # Combine data from dict_list1
    for d in dict_list1:
        name = d['name']
        units = d['units']
        if name in combined_dict:
            combined_dict[name]['units'] += units
        else:
            combined_dict[name] = {'name': name, 'units': units}

    # Combine data from dict_list2
    for d in dict_list2:
        name = d['name']
        units = d['units']
        if name in combined_dict:
            combined_dict[name]['units'] += units
        else:
            combined_dict[name] = {'name': name, 'units': units}

    return list(combined_dict.values())


# Example usage
dict_list1 = [{'name': 'apple', 'units': 5}, {'name': 'banana', 'units': 10}]
dict_list2 = [{'name': 'banana', 'units': 15}, {'name': 'apple', 'units': 3}]

combined_data = combine_dicts(dict_list1, dict_list2)
print(combined_data)
