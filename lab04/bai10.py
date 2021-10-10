def db_headings(dict_of_dict):
    inner_keys = set()
    for key in dict_of_dict:
        for inner_key in dict_of_dict[key]:
            inner_keys.add(inner_key)
    return inner_keys
print(db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}}))