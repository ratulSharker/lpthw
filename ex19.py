def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for a party!")
    print("Get a blanket\n")

print("We can just pass two numbers to the function directly")
cheese_and_crackers(100, 30)

print("OR, We could assign values to a variable and then call the function")
cheese_count = 102
boxes_of_crackers = 14
cheese_and_crackers(cheese_count, boxes_of_crackers)

print("We can do math inside the function call")
cheese_and_crackers(100*3, 90*2)

print("And we can combine the two")
cheese_and_crackers(cheese_count + 2, boxes_of_crackers*2)