the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# This first kind of for loops goes through a list
for number in the_count:
    print(f"This is count {number}")

# Same as above
for fruit in fruits:
    print(f"This is fruit {fruit}")

# Here comes the mixed list
for i in change:
    print(f"I got {i}")

# Now we can build list
elements = range(0, 10)

# Then use the range function to do 0 to 10 count
# for i in range(0, 10):
#     print(f"Appending {i} in list")
#     elements.append(i)

# Printing the added elements
for i in elements:
    print(f"Element was {i}")
