my_list = [1, 2, 3, 2, 1, 4]

def get_unique_list(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i) 
    return new_list

unique_list = get_unique_list(my_list)
print(unique_list)