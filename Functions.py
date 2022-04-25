
def say_hi():
    print("Hello world!")


print("Top")
say_hi()
print("Bottom")

# A parameter is a piece of information that we provide to function
def say_hi(name):
    print("Hello! " + name + "\n" + "How are you ?")


say_hi("Mikey")
say_hi("John")
say_hi("Stevie")

                            # RETURN STATEMENT
def cube(num):
    return (num * num * num)

result = cube(4)
print(result)

