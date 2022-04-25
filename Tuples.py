# It is a type of data structure. it is a container where we store different values.
# Tuples are immutable, they can't be changed.

my_list = ("chair", "book", "car", "pencil")
my_tuple = ("mango", "apple", "grapes", "cherry", "banana")
print(my_tuple)
# ('mango', 'apple', 'grapes', 'cherry', 'banana')
print(type(my_tuple))
# <class 'tuple'>
print(my_list)
# ('chair', 'book', 'car', 'pencil')
print(type(my_list))
# <class 'tuple'>

# add other tuple to the primary one.
print(my_tuple.__add__(my_list))
# ('mango', 'apple', 'grapes', 'cherry', 'banana', 'chair', 'book', 'car', 'pencil')
print(my_tuple.count("banana"))
# 1
print(my_tuple.index("banana"))
# 4
print(my_tuple.__add__(my_list).__contains__("chair"))
# True
print(my_list.__contains__("car"))
# True

