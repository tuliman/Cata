from  itertools import groupby

def unique_in_order(iterable):
    data = []
    for key,group in groupby(iterable):
        data.append(key)

    return data

unique_in_order('AAAABBBCCDAABBB')

