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

