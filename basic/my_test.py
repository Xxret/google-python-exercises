def linear_merge(list1, list2):
    new_list = []
    while len(list1) and len(list2):
        if list1[0] <= list2[0]:
            new_list.append(list1.pop(0))
        else:
            new_list.append(list2.pop(0))
    new_list.extend(list1)
    new_list.extend(list2)
    return new_list

print linear_merge([1,2,3,4], [5,6,7,8,9])

