from collections import Iterable


def is_path(a):
    a_list = a.split('/')
    if a_list[0] != '' or a_list[1] == '':
        return False
    else:
        return True


def is_paths(a):
    if not isinstance(a, Iterable):
        raise TypeError('The object is not iterable')
    r = []
    for i in a:
        r.append(is_path(i))
    if all(r):
        return True
    else:
        return False
