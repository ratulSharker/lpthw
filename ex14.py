from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, i am the {script} script")
print("I would like to ask you some question")
print(f"1. Do you like me {user_name} ?")
likes: str = input(prompt)

print(f"2. Where do you live {user_name} ?")
address: str = input(prompt)

print(f"3. What kind of computer do you have ?")
computer: str = input(prompt)

print(f"""
    Alright "{user_name}",
    You said "{likes}" about liking me
    You live in "{address}"
    And you have "{computer}" computer. Nice.
    """)

# run it like `python ex14.py "Whatever name"`
