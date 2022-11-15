#Lists: ordered, mutable, allows duplicate elements

my_list = ["banana","cherry","apple"]
my_list2 = [1,2,3,4,5]

print(my_list)

# my_list2 = list()

# print(my_list2)

# #list allows different data types :

# my_list3 = [5, True,"apple","apple"]
# print(my_list3)

# item = my_list[0]
# item2 = my_list[-1] #represents last item

# print(item)
# print(item2)

# for i in my_list:
#     print(i)

# if "banana" in my_list:
#     print("yes")
# else:
#     preint("no")

#checking how many elements in my_list
print(len( my_list))

my_list.append("5")
print(my_list)

#insert item in specific position
my_list.insert(1, "blueberry") #at index 1 we will have blueberry
print(my_list)

#remove items
deleted = my_list.pop()
print(deleted)
print(my_list)

#remove specific elemet
item_delete = my_list.remove("cherry")
print(item_delete)


#remove all items with clear method

#reverse the list
item = my_list.reverse()

#sort the list with sort method

item = my_list.sort()

#concat two list

concat_list = my_list + my_list2
print(concat_list)

#Slicing the list

new_list = [1,2,3,4,5,6,7,8,9]

another_list = new_list[1:5]
print(another_list)


b = [i*i for i in my_list]
print(b)