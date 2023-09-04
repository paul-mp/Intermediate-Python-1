my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

#utilized this for help: https://stackoverflow.com/questions/69205854/iterating-over-dictionary-in-python-and-using-each-value

def get_combined_dict(my_dict_1, my_dict_2):
    new_dict = {}
    for key in my_dict_1:
        if key in my_dict_2:
            new_dict[key] = my_dict_1[key] + my_dict_2[key]
    return new_dict

combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
