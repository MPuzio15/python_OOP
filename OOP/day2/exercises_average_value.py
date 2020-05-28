from functools import reduce
from statistics import mean

temperatures = [10.1, 12.31, 15.13, 14.13, 4.31, 13.10, 12.02]


def returnHigher(array):
    sum = reduce(lambda x, y: x + y, array)
    average = sum / len(array)
    higher_than_average = filter(lambda x: x > average, array)
    return (list(higher_than_average))

print(returnHigher(temperatures))

def new_list2(array):
     #srednia
     higher = filter(lambda x: x>mean(array), array)
     return higher

print(list(new_list2(temperatures)))
