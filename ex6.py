types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those {do_not}"

print(x)
print(y)

print(f"i said {x}")
print(f"i also said {y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}"

print(joke_evaluation.format(hilarious))

w = "This is left side of ..."
e = "This is the right side."
print(w + e)