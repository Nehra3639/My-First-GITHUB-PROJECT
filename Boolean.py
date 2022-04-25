# IF statement allows program to respond to the input that given.

is_male = True
if is_male:
    print("you are a male")


is_male = False
if is_male:
    print("you are a male")
else:
    print("you are a female")

# CONDITION - 1
is_male = True
is_tall = True
if is_male or is_tall:
    print("you are a male or tall")
else:
    print("you neither male nor tall")

# CONDITION - 2
is_male = True
is_tall = False
if is_male or is_tall:
    print("you are a male or tall")
else:
    print("you neither male nor tall")

# CONDITION - 3
is_male = False
is_tall = False
if is_male or is_tall:
    print("you are a male or tall")
else:
    print("you neither male nor tall")

