
# CONDITION - 1
is_male = True
is_tall = True
if is_male or is_tall:
    print("you are a tall male")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are not a male but tall")
else:
    print("you are not a tall nor a male ")


# CONDITION - 2
is_male = True
is_tall = False
if is_male or is_tall:
    print("you are a tall male")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are not a male but tall")
else:
    print("you are not a tall nor a male ")

# CONDITION - 3
is_male = False
is_tall = True
if is_male or is_tall:
    print("you are a tall male")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are not a male but tall")
else:
    print("you are not a tall nor a male ")

# CONDITION - 4
is_male = False
is_tall = False
if is_male or is_tall:
    print("you are a tall male")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are not a male but tall")
else:
    print("you are not a tall nor a male ")


                #   "IF Statement & Comparisions"  #
def max_num(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
    elif num2 >= num1:
        if num2 >= num3:
            return num2
        else:
            return num3


print(max_num(3, 4, 5))
