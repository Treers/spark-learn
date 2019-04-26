def is_path(a):
    a_list = a.split('/')
    if a_list[0] != '' or a_list[1] == '':
        return False
    else:
        return True
