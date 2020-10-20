"""
Dictionary
🔑 Allow to store data in key-value pairs
🔑 Dictionaries are MUTABLE
🔑 Keys can only be IMMUTABLE types
🔑 We use dictionaries when we want to be able to quickly access additional data associated with a particular key

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/60-dictionaries/
"""

# 🛠 Declaration
phone_prices = {"16gb": 200, "32gb": 400, "64gb": 500}
# print(len(phone_prices))
# print(phone_prices["16gb"])

# 🛠 Adding and removing
phone_prices["128gb"] = 700
# print(phone_prices)

# 🛠 Updating
phone_prices["128gb"] = 800
# print(phone_prices)

# 🛠 Complex dictionary
phone_list = {
	"iphone5s": {
		"color": ["black", "white"],
		"prices": {"16gb": 200, "32gb": 400, "64gb": 500}
	},
	"iphone6": {
		"color": ["space-gray", "white"],
		"prices": {"16gb": 300, "32gb": 500, "64gb": 600}
	}
}
# print(phone_list["iphone6"])

# 🛠 Items, Keys and Values
# Get all keys in the dictionary
# print(phone_list.keys())

# Get all values in the dictionary
# print(phone_list.values())

# Get all items (keys, values, pairs) in a dictionary
phone_items = phone_list.items()
print(type(phone_items))
# print(phone_items)