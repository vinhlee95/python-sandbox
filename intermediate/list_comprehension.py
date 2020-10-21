"""
List comprehension

🔑 Can create a list by wrapping [] around a for loop
🔑 Can use Conditional within a list comprehension
🔑 Can use String joining with a list comprehension
🔑 Can use Math functions. Handy with conditions
"""

# 🛠 List comprehension
names = ["Harry", "Ron", "Hermione", "Dumberdore"]
greet_names = [f'Hi {name}' for name in names]
name_length = [len(name) for name in names]
# print('Say hi to everyone:', greet_names)
# print('Name length is:', name_length)

# 🛠 Conditional
long_name_list = [name for name in names if len(name) > 5]
# print('Long name list is:', long_name_list)

# 🛠 String joining
greet_names_string = ', '.join([f'Hi {name}' for name in names])
print(greet_names_string)

# 🛠 Math functions (min, max, sum)
number_list = range(0, 100)
# print('Max number is:', max(number_list))
total_sum = sum([num for num in number_list])
# print('Total sum is:', total_sum)
# ⭐️ But there is a simpler way to do this:
# print(sum(number_list))

# 🔑 What comes in handy is to do match functions with conditions
# 🛠 Calculate sum of all odd numbers
odd_sum = sum([num for num in number_list if num % 2 == 1])
# print('Total sum of all odd numbers is:', odd_sum)