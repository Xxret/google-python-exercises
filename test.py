def helper_fun(file):
    f = open(file, 'r')
    f_tran_str = f.readinto()
    f.close()
    f_tran_str.lower()
    list_1 = f_tran_str.split()
    list_2 = sorted(list_1)
    new_dict = {}
    for word in list_2:
        if word not in new_dict.keys():
            new_dict[word] = 1
        else:
            new_dict[word] += 1
    return new_dict

def print_words(file):
    new_dict2 = helper_fun(file)
    list_of_tuples1 = new_dict2.items()
    for item in dict2_to_list:
        print item
    sys.exit(0)

def print_top(file):
    new_dict3 = helper_fun(file)
    list_of_tuples2 = new_dict3.items()
    def sort_last(tuple):
        return tuple[-1]
    new_of_tuples2 = sorted(list_of_tuples2, key=sort_last)
    return new_of_tuples2[-20:]

print print_top('alice.txt')