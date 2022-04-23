# this is just like `argv`
def print_two(*args):
    arg1, arg2 = args
    print(f"Arg1 = {arg1}, Arg2 = {arg2}")

# this one takes two argument
def print_two2(arg1, arg2):
    print(f"Arg1 = {arg1}, Arg2 = {arg2}")

# this one takes one argument
def print_one(arg1):
    print(f"Arg1 = {arg1}")
    
# this one does not take any argument
def print_no_arg():
    print("No argument to print")

print_two("hello", "world")
print_two2("One", "Two")
print_one("Hello world")
print_no_arg()