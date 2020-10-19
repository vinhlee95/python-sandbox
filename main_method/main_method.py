"""
The main method
- Make sure that "main" method is only run when it is executed as a stand-alone program

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/175-running-code/30-the-main-method/
"""
def find_item(item, list):
	if bool(list) == False:
		return
	index = list.index(item)

	# This code is NOT be run when it is imported by other modules
	if __name__ == "__main__":
		print("Found index:", index)

	return index
