#tuple: ordered,immutable, allows duplicate elements

# mytuple = ("max",28,"Boston")
# print(mytuple)

# mytuple2 = tuple(["max",11,22])
# print(mytuple2)

# item = mytuple[0]
# print(item)

# for i in mytuple2:
#     print(i)

my_tuple =('a','b','c','d','e','f','g','h')

print(len(my_tuple))

print(my_tuple.count('a'))

print(my_tuple.index('a')) #we get the index of a 

my_list = list(my_tuple)
print(my_list)

#unpacking 

my_tuple3 = "max",20,"kathmandu"

name,age,city = my_tuple3
print(name)
print(age)
print(city)

my_tuple4 = [0,1,2,3,4]

i1, *i2, i3 = my_tuple4

print(i1)
print(i3)
print(i2)



