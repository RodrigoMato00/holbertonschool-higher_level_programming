#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
     return (0)
    return sum(tuple(i * j for i, j in my_list))/sum(k[1] for k in my_list)
