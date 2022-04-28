people = 30
cars = 40
trucks = 15

if cars > people:
	print("There is enough cars for each person")
elif cars < people:
	print("There is not enough car for each person")
else:
	print("We can't decide")

if trucks > cars:
	print("That's too many trucks")
elif trucks < cars:
	print("Maybe we could take the trucks")
else:
	print("We still can't decide")

if people > trucks:
	print("There is enough trucks for each person")
else:
	print("There might not be enough trucks for each person")
