
print("Inheritance Example", end="\n\n")
# Inheritance
class Parent(object):

	def implicit(self):
		print("Parent implicit method called")

	def override(self):
		print("Parent override method called")

	def altered(self):
		print("Parent altered method called")

class Child(Parent):
	
	def override(self):
		print("Child override method called")

	def altered(self):
		print("Before parent altered, child altered")
		super(Child, self).altered()
		print("After parent altered, child altered")

dad = Parent()
son = Child()

# implicit test
dad.implicit()
son.implicit()

# override test
dad.override()
son.override()

# altered test
dad.altered()
son.altered()


print("Composition Example", end="\n\n")
# Composition
class Other(object):

	def implicit(self):
		print("Other implicit called")
	
	def override(self):
		print("Other override called")

	def alter(self):
		print("Other altered called")

class Person(object):

	def __init__(self):
		self.parent = Other()
	
	def implicit(self):
		self.parent.implicit()
	
	def override(self):
		print("Person override called")
	
	def alter(self):
		print("Before other altered")
		self.parent.alter()
		print("After other altered")

other = Other()
person = Person()

person.implicit()

person.override()

person.alter()