"""
Control statements
- If, else, elif
- Break, continue, return

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/110-control-statements-looping/40-break-continue/
"""

# 🔑 Break statement completely break out the loop
names = ["Harry", "Ron", "Hermione", "Sirius", "Severus"]
# for name in names:
# 	print(f"{name}")
# 	if name == "Ron":
# 		break

# 🔑 Continue statement skip current interation and move to the next one
# for name in names:
# 	if name == "Hermione":
# 		continue
# 	if name == "Sirius":
# 		break
# 	print(name)

# 🔑 break and continue only work for THE CURRENT LOOP
# for name in names:
# 	print(f"{name} in outer loop")
# 	for char in name:
# 		if char == "s":
# 			print("Break the inner loop at name:", name)
# 			break

# 🔑 Return statement kill the loop completely
# def find_name(target):
# 	for index, name in enumerate(names):
# 		if name == target:
# 			print(f"Found {name} in position {index}")
# 			return name

# find_name("Sirius")


