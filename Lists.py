# Lists are built-in data types used to store collections of data.
# lists are used to store multiple items in a single variable.

friends = ["kevin", "karen", "jim", "mikey"]
print(friends)
# ['kevin', 'karen', 'jim', 'mikey']
print(type(friends))
# <class 'list'>

                                            # indexing
print(friends[0])
# kevin
print(friends[-1])
# mikey
print(friends[1:])
# ['karen', 'jim', 'mikey']

                                        # Lists functions
lucky_num = [4, 26, 15, 9, 33, 75]
Friends = ["kevin", "karen", "jim", "mikey", "toby", "oscar", "mikey"]
Friends.extend(lucky_num)
print(Friends)
# ['kevin', 'karen', 'jim', 'mikey', 'toby', 'oscar', 'mikey', 4, 26, 15, 9, 33, 75]

Friends.append("creed")
print(Friends)
# ['kevin', 'karen', 'jim', 'mikey', 'toby', 'oscar', 'mikey', 4, 26, 15, 9, 33, 75, 'creed']

Friends.insert(1, "kelly")
print(Friends)
# ['kevin', 'kelly', 'karen', 'jim', 'mikey', 'toby', 'oscar', 'mikey', 4, 26, 15, 9, 33, 75, 'creed']

Friends.remove("jim")
print(Friends)
# ['kevin', 'kelly', 'karen', 'mikey', 'toby', 'oscar', 'mikey', 4, 26, 15, 9, 33, 75, 'creed']

Friends.pop()
print(Friends)
# ['kevin', 'kelly', 'karen', 'mikey', 'toby', 'oscar', 'mikey', 4, 26, 15, 9, 33, 75]

print(Friends.index("oscar"))
# 5

print(Friends.count("mikey"))
# 2

my_list = ["kevin", "creed", "kelly", "karen", "mikey", "toby", "oscar", "john"]
my_list.sort()
print(my_list)
# ['creed', 'john', 'karen', 'kelly', 'kevin', 'mikey', 'oscar', 'toby']

my_list.reverse()
print(my_list)
# ['toby', 'oscar', 'mikey', 'kevin', 'kelly', 'karen', 'john', 'creed']

her_list = my_list.copy()
print(her_list)
# ['toby', 'oscar', 'mikey', 'kevin', 'kelly', 'karen', 'john', 'creed']

