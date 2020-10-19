"""
Exception and Traceback
🔑 An uncaught exception will quit the running Python program
🔑 Use try and except to catch exceptions
🔑 Try to catch the exceptions as specific as possible (SyntaxError, ValueError...)
🔑 Use "as" to access the exception

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/175-running-code/50-exceptions/
"""
# 🛠 Catch a value error
# try:
# 	int("a")
# except ValueError:
# 	print("Cannot convert that value into string")

# 🛠 Access an exception
# try:
# 	int("a")
# except ValueError as error:
# 	print("Cannot convert that value into string", error)