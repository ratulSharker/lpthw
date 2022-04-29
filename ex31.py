print("""You enter a dark room with two doors.
Do you go through door #1 or door #2 ?""")

door = input("> ")

if door == "1":
    print("""There is a giant bear here, eating cheese cake
What do you do ?
1. Take the cake.
2. Scream at the bear.""")
    
    action = input("> ")
    
    if action == "1":
        print("The bear eats your face off. Good job!")
    elif action == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Doing {action} was probably better.")
        print("Bear runs away.")

elif door == "2":
    print("""You Stare into the endless abyss of Cthulhu's eye.
          1. Blueberries
          2. Yellow jacket clothespins.
          3. Understanging revolvers yelling melodies.""")
    action = input("> ")
    
    if action == "1" or action == "2":
        print("Your body survives powered by a mind of jello")
        print("Good job")
    else:
        print("The insanity rots your eyes into a pool of muck.")
else:
    print("You stumbled around and fall on a knife and die. Good job!")
