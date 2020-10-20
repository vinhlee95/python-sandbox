"""
Handling File in Python
🔑 Can use Context Manager to wrap around a block of code that depends on some resources
🔑 When exiting the scope, the context manager will automatically do the cleaning up by closing opened files, even if the code hits exception within the context manager

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/175-running-code/60-working-with-files/
"""
import json
import pathlib

# 🛠 Perform all functions that require access to the open file within "with" scope
current_path = pathlib.Path(__file__).parent.absolute()

with open(f"{current_path}/data.json") as data:
	keyword_data = json.load(data)
	print("Keyword is:", keyword_data["keyword"])