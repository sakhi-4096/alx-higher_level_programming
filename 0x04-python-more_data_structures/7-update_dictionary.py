#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        dict2 = {key: value}
        a_dictionary.update(dict2)
        return (a_dictionary)
    else:
        return None
