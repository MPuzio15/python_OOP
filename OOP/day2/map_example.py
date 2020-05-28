#map - iterates throught all array elements and do sth - returns new array
#lazy evaluation - its crucial to have as few
x =list(range(0,31))
even = list(filter(lambda elem: elem % 2 == 0,x))
print(even)
sqrt_num = list(map(lambda elem: elem **2, even))
print(sqrt_num)

# inOneLine = map(lambda x: x%2==0, filter(lambda x: x**2 == 0), x)
#
# print(list(inOneLine))