def add(a, b):
    print(f"ADDING {a} + {b}")
    return a+b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divide(a, b):
    print("DIVIDING {a} / {b}")
    return a/b

print("Lets do some maths with our function")

age = add(a = 10, b = 20)
height = subtract(a = 50, b = 3)
weight = multiply(a = 10, b = 5)
iq = divide(a = 10, b = 3)

print(f"Age {age}, Height {height}, weight {weight}, iq {iq}")
