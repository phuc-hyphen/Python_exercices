def addition(a, b):
    sum = a + b
    print("Sum of two numbers is:", sum)

    addition(5, 6)


def language(lname):
    print("Current language is:", lname)


language(lname="Python")


def country(cName="India"):
    print("Current country is:", cName)


country("NewYork")
country("London")
country()

# * allow us to pass non-fixed/variable number of arguments
def add(*num):
    sum = 0
    for n in num:
        sum = n + sum
    print("Sum is:", sum)
add(2, 5)
add(8, 78, 90)

# ** allow us to pass non-fixed/variable number of arguments with keywords
def employee(**data):
    for (key, value) in data.items():
        print(" The value {} is {}".format(key, value))
employee(Name="John", Age=20)
employee(Name="John", Age=20, Phone=123456789)
