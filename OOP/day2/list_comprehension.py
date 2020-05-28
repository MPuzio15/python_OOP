even_numbers = []
for x in range(0,30):
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)

#list comprehension
#we declare x and the array range, than we declare the array condition
even_numbers2 = [ x
                  for x in range(0,30)
                  if x % 2 == 0
                ]

print(even_numbers2)

squered_even_numbers = [ y ** 2 for y in even_numbers2]

print(squered_even_numbers)

#conditions
fruits = [x for x in [1,2,4,6,8,9]  if x <8]

print(fruits)

germs = ["bacteria", "viruses", "fungus"]
no_virus = [v for v in germs if v!="viruses"]
print(no_virus)






