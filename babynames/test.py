import re

def extract_names(filename):
    f = open(filename, 'rU')
    strings = f.read()
    f.close()
    match_year = re.search(r'Popularity in (\d\d\d\d)', strings)
    if match_year:
        print match_year.group(1)

    namerank_dict = {}
    match_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td>', strings)
    if match_names:
        print match_names
    for each_name in match_names:
        namerank_dict[each_name[1]] = each_name[0]
    print namerank_dict
    names_list = namerank_dict.keys()
    rank_list = namerank_dict.values()
    namerank_list = []
    for i in range(len(names_list)):
        namerank_list.append(names_list[i] + ' ' + rank_list[i])
    sort_namerank_list = sorted(namerank_list)
    print sort_namerank_list
    sort_namerank_list.insert(0, match_year.group(1))
    print sort_namerank_list


extract_names('baby1992.html')