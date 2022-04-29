def fill_up_number(upto: int, increments_by : int):
    i = 0
    numbers = []

    while i <= upto:
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i += increments_by
        print(f"Numbers now {numbers}")
        print(f"i is now {i}")
    
    return  numbers

print("The numbers")
for number in fill_up_number(3, 2):
    print(number)
    