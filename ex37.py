## Keywords

# and
print("Example `and`")
if 1 == 1 and 2 == 2:
    print("one equal to one `and` two equal to two", end="\n\n")

# with as
print("Example `as`")
with open('ex37.py') as f:
    first_line = f.readline()
    print(first_line, end='\n\n')

# assert
print("Example `assert`", end='\n\n')
a = 5
b = 2
assert b != 0, "zero denominator is not allowed"
a = a/b

# break
print("Example `break`")
my_list = [1, 2, 3, 4, 5, 6]
for number in my_list:
    print(f"Number seen {number}")
    if number == 3:
        break
print("", end="\n")

# class
class ComplexNumber:

    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i"
    
    def add_real(self, real: float):
        self.real += real 
    
    def add_imaginary(self, imaginary: float):
        self.imaginary += imaginary

z = ComplexNumber(1.2, 2.1)
z.add_real(2)
print(z)

# class inheritance
class Car:

    def __init__(self, brand) -> None:
        self.brand = brand

class Toyota(Car):

    def __init__(self, model) -> None:
        # super().__init__("Toyota")
        Car.__init__(self, "Toyota") # same as calling `super()`
        self.model = model

land_cruiser = Toyota("Land Cruiser")
print(land_cruiser.brand)
print(end="\n\n\n")

# continue
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if number % 2 == 0:
        # conitnue for even number
        continue
    # only odd numbers are printed
    print(number)

print(end="\n\n\n")

# def
def sum(a, b):
    return a+b

print(sum(1, 2))
print(end="\n\n\n")

# elif
if False:
    print("This print is never going to be printed")
elif True:
    print("This statement inside `elif` will appear")

print(end="\n\n\n")

# else
if False:
    print("This line will never printed")
else:
    print("This line inside `else` will be printed")

print(end="\n\n\n")

# except - try
try:
    print(1+"1")
except TypeError as err:
    print(err)

# finally
try:
    print(name_not_declared)
except NameError as err:
    print(err)
finally:
    print("Anyway this block inside the `finally` will appear")

# for
arr = [1, 2, 3, 4, 5]
for number in arr:
    print(number)

# from - import
from os import getcwd
print(getcwd())

# global
global_scopred_variable = "a"

def some_function():
    global global_scopred_variable
    global_scopred_variable = "b"

some_function()
print(global_scopred_variable)

# if
if True:
    print("This line going to be printed anyway")

# in
if 1 in [1, 2, 3, 4]:
    print("one is inside `one`, `two`, `three`, `four`")

# is
one = 1
if 1 is one:
    print("1 is one")

# lambda
square = lambda x: x * x
print(square(4))

# not
if not False:
    print("not False means True")

# or
if 1 or False:
    print("1 or False, evaluates to True")

# pass
def pass_if_val_is_one(val: int):
    if val == 1:
        pass
    else:
        print("not pass")

pass_if_val_is_one(1)
pass_if_val_is_one(2)

# print
print("Print this string")

# raise
try:
    raise NameError("casually raising an exception")
except NameError as err:
    print(err)

# return
def add(a: int, b: int):
    return a+b

print(add(1, 2))

# while
index = 1
while index < 10:
    print(index)
    index += 1

# yield
def odd_number_generator():
    odd_number = 1
    while odd_number < 10:
        yield odd_number
        odd_number += 2

odd_numbers = odd_number_generator()

for odd_number in odd_numbers:
    print(odd_number)
