"""
Class
"""

# 🛠 Create class
class User:
	# Constructor
	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age

	# Method
	def greeting(self):
		print(f'Hi {self.name}')

# Init user object
me = User("Vinh", "foo@bar.com", 25)
# me.greeting()

# 🛠 Inheritance
class Customer(User):
	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age
		self.balance = 0

	def set_balance(self, balance):
		self.balance = balance

customer1 = Customer('Foo', 'foo@bar.co', 13)
customer1.set_balance(10)
customer1.greeting()
print('Your balance is:', customer1.balance)