def helper_fun(file):
    f = open(file, 'r')
    f_tran_str = f.read()
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
    new_dict_2 = helper_fun(file)
    list_of_tuples1 = new_dict_2.items()
    for item in list_of_tuples1:
        print item


def print_top(file):
    new_dict3 = helper_fun(file)
    list_of_tuples2 = new_dict3.items()
    new_tuples2 = sorted(list_of_tuples2, key=lambda x: x[1], reverse=True)
    list_of_tuples3 = new_tuples2[:20]
    print list_of_tuples3


