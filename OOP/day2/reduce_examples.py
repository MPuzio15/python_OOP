#reduce - przechodzi po kazdym elemencie 0 i 1 i
#cos z nimi robi np mnozy i zastepuje te dwa pierwszym,
#i idzie dalej uzywa juz tego nowego i kolejnego jeszcze
#nie zmienionego

from functools import reduce

temperates = [10.1, 12.31, 15.13, 14.13, 4.31]

temp_variable = 0
for x in temperates:
    temp_variable += x
print(temp_variable)

print(sum(temperates))

def multiply(elem1, elem2):
    return elem1 * elem2



print(temp_variable)
print(sum(temp_variable))

with_reduce = reduce(lambda arg1,arg2: arg1*arg2, temperates)
print(with_reduce)

