print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print("\n newlines \t tabs")

poem = """
\tThe loverly world
with logic so firmly planted
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five : {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 100
beans, jars, crates = secret_formula(start_point)

# Remember that, this is another way of format a string
print("With a starting point of: {}".format(start_point))
print(f"We'd have beans {beans}, jars {jars}, crates {crates}")


print("We can also do that this way")
start_point = start_point / 10
formula = secret_formula(start_point)
print("beans {}, jars {}, creates {}".format(*formula))