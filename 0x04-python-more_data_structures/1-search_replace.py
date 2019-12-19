#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    [(new.append(i) if i != search else new.append(replace)) for i in my_list]
    return new
