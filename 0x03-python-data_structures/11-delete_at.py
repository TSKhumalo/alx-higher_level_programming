#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    elif idx == 0:
        del my_list[0]
        return my_list
    elif my_list:
        del my_list[idx]
        return 
