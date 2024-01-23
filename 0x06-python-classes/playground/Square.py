class Square:
	def __init__(self, height="0", width="0") -> None:
		self.height = height
		self.width = width

	@property
	def height(self):
		print("Retrieving the height")
		return self.__height
	
	@height.setter
	def height(self, value):
		if value.isdigit():
			self.__height = value
		else:
			print("Please only enter numbers for height")

	@property
	def width(self):
		print("Retrieving the width")
		return self.__width
	
	@width.setter
	def width(self, value):
		if value.isdigit():
			self.__width = value
		else:
			print("Please only enter numbers for width")
	
	def getArea(self):
		return int(self.__width) * int (self.__height)
	
def main():
	aSquare = Square()

	height = input("Enter Width: ")
	width = input("Enter Weight: ")

	print("The area is: ", aSquare.getArea())

	aSquare.height = height
	aSquare.width = width

	print("Height :", aSquare.height)
	print("Width :", aSquare.width)

	print("The area is: ", aSquare.getArea())


main()