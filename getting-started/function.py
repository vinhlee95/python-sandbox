"""
Functions

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/060-functions/
"""
# 🛠 Functions
def printName(name):
	gretting = "Hello"
	print(f"{gretting} {name}")
# printName("Vinh")

# 🛠 Default parameter
def sayName(name = "Vinh"):
	gretting = "Hi"
	print(f"{gretting} {name}")
# sayName()

# 🛠⚠️ Don't do this
def addToList(item, list = []):
	"""
	Append item to a list

	Parameters
	----------
	item: any
		the value that we want to append to the list
	list: list
		the default list (default: [])

	‼️ This function will not work properly since the list does not reset its value
	every time we call this function.
	"""

	list.append(item)
	print("List is: ", list)
# addToList(1) # expect: [1]
# addToList(2) # expect: [2] BUT the computer says NO

# 🛠✅ Do this
def appendToList(item, list = None):
	if list is None:
		list = []
	list.append(item)
	print("Correct list is: ", list)
# appendToList(1) # [1]
# appendToList(2) # [2]

# 🛠 Function scopes
x = 1
y = 2
def calculate_sum(x, y):
	print("Sum is: ", x + y)
# print("Outside of calculate_sum scope: ", x, y)
# calculate_sum(4,5)

# 🛠 Positional arguments vs. Keyword arguments
def do_math(x, y, type = "add"):
	"""
	Calculate a math operation from 2 provided numbers
	depending on which type the calculation is

	Parameters
	----------
	x: int
		the first number
	y: int
		the second number
	type: string
		the type of operation (default: "add")
	"""

	if type == "add":
		return x + y
	elif type == "subtract":
		return x - y

	print("Calculation type is not supported:", type)

sum_result = do_math(1,2)
subtract_result = do_math(5, 4, "subtract")
# multiply_result = do_math(1, 3, "multiply")
# print("Sum result is:", sum_result)
# print("Subtract result is:", subtract_result)