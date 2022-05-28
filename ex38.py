ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuffs = ["Day", "Night", "Song", "Frisbee",
				"Corn", "Banana", "Girl", "Boy"]

# Regular while loop
# while len(stuff) != 10:
# 	next_one = more_stuffs.pop()
# 	print("Adding: ", next_one)
# 	stuff.append(next_one)
# 	print(f"There are {len(stuff)} items now.")

# Same implementation using for-loop
for next_one in reversed(more_stuffs):
	if len(stuff) == 10:
		break
	else:
		stuff.append(next_one)

print("There we go : ", stuff)

print("Lefs do some things with stuffs")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))


# Study drills
days_in_a_week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
print("Days in a week are : ", ",".join(days_in_a_week))

month_in_a_year = ["January", "February", "March", "April", "May",
                   "June", "July", "August", "September", "October", "November", "December"]
print("Months in a year are : ", ",".join(month_in_a_year))

programming_language_i_know_so_far = ["C", "C++", "Java", "Swift", "Objective-C", "Javascript"]
print("Programming languages in know so far : ", ",".join(programming_language_i_know_so_far))

