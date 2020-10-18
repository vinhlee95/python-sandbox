"""
Boolean logic
🔑 Empty sequences (set, list, dictionaries) are evaluated as False
🔑 Equality operators (==, !=) compare CONTENT of 2 different values
🔑 Identity (is, is not) checks for identity of 2 values in memory

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/090-boolean-logic/20-comparisons/
"""

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]

# print("They should have similar content:", list_1 == list_2)
# print("They are 2 same lists:", list_1 is list_2)

# 🛠 And, or, not
a = True
b = False
# print(a or b)

phone_list = ["iphone", "galaxy", "pixel"]
has_items = bool(phone_list)
has_iphone = "iphone" in phone_list
has_oppo = "oppo" in phone_list
# print(has_items and has_iphone)
# print(has_items and has_oppo)
