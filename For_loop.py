friends = ["kevin", "creed", "kelly", "oscar", "john"]
for index in range(5):
    if index == 2:
        print("first iteration")
    else:
        print("not first")

#using len inplace of range
for index in range(len(friends)):
    if index == 2:
        print("first iteration")
    else:
        print("not first")


for index in range(len(friends)):
    print(friends[index])

# Exponent func
print(2**3)

base_num = True
pow_num = True

def raise_to_power(base_num, pow_num):
    return base_num * base_num * base_num
result = 1
for index in range(pow_num):
    result = (result * base_num)


print(raise_to_power(5,2))

