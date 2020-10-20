"""
Tuple data type

Tuples are light-weight collections used to keep track of related, but different items. Tuples are immutable, meaning that once a tuple has been created, the items in it can’t change.

Tuples are different in a few ways. While lists are generally used to store collections of similar items together, tuples, by contrast, can be used to contain a snapshot of data. They can’t be continually changed, added or removed from like with a list.

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/30-tuples/
"""
# 🛠 Creation
parts = ("gas_tank", 1000, "liters", "wheels", 4, "items")
print(type(parts))

# 🛠 Accessing
print("First item:", parts[0])

# ⚠️ Cannot change items in a tuple
# parts[0] = "seats" # TypeError: 'tuple' object does not support item assignment

# 🎁 Unpacking
gas, gas_amount, gas_measurement, wheel, wheel_amount, wheel_measurement = parts
# print(gas, gas_amount, gas_measurement)

def handle_error():
	return 400, "Bad request"
status_code, error_message = handle_error()
print(status_code, error_message)

