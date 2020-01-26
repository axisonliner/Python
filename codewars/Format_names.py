#  File name: Format_names.py
#  Developed by Yuriy Kondrashov on 1/26/20 2:49 PM
#  Date last modified: 1/26/20 2:48 PM
#  Copyright (c) 2020. All rights reserved.

def namelist(names):
    # return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ", 1)[::-1]

    list_names = []
    for x in names:
        list_names.append(x['name'])
    if list_names:
        if len(list_names) >= 2:
            return ', '.join(list_names[:-1]) + " & {}".format(list_names[-1])
        else:
            return ''.join(list_names)
    else:
        return ""




if __name__ == "__main__":
    print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
# 'Bart, Lisa, Maggie, Homer & Marge', "Must work with many names")
    print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# returns 'Bart, Lisa & Maggie'
    print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# returns 'Bart & Lisa'
    print(namelist([{'name': 'Bart'}]))
# returns 'Bart'
    print(namelist([]))
# returns ''