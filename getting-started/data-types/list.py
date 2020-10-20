"""
List data type

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/10-lists/
"""

# 🛠 Basics
name_list = ["Harry", "Ron", "Frank", "Hermione"]
# print("First name of the list is:", name_list[0])
# print("Amount of names is:", len(name_list))

# 🛠 Sorting a copy of the list
def sort_list(list, reverse = False):
	if list != None:
		return sorted(list, reverse=reverse)
	print("List must exist")

# sorted_list = sort_list(name_list)
# print("Original list: ", name_list)
# print("Sorted list:", sorted_list)
# print("Reverse list:", sort_list(name_list, True))

# 🛠 Sorting in-place
# name_list.sort(reverse=False)
# print("Original list:", name_list)

# 🛠 Adding items
name_list.append("Lupin")
# print(name_list)

name_list.insert(len(name_list), "James")
# print(name_list)
# ['Harry', 'Ron', 'Frank', 'Hermione', 'Lupin', 'James']

# 🛠 Looking for item
hasHarry = "Harry" in name_list
# print("List has Harry:", hasHarry, name_list.index("Harry"))

# 🛠 Removing items
name_list.pop()
# print(name_list)

name_list.pop(0)
print(name_list)