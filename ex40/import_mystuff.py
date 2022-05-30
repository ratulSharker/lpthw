import mystuff

mystuff.apple()
print(mystuff.tangerine)


# Equivalent class
class MyStuff:

	def __init__(self) -> None:
		self.tangerine = "Tangerine is a color"
	
	def apple(self):
		print("This is classy apple")

mystuff_obj = MyStuff()
mystuff_obj.apple()
print(mystuff_obj.tangerine)