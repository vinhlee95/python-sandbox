"""
Asterisks in Python
"""

# Keyword arguments
def greet(name, message='Hi there'):
	print(f'{message} {name}')

# Normal arguments
# greet('Foo', 'Hello world')
# Keyword arguments
# greet(name='Foo')
# greet(message='Hello there', name='Bar')

# Arbitrary arguments
def say_names(*names):
	for name in names:
		print(f'Hi {name}')

# say_names('Harry', 'Ron', 'Hermione')

# Unpacking into function call
phones = ['iPhone', 'pixel', 'galaxy']
# print(*phones)

# Capture keyword arguments given to the function into a dictionary
def tag(tag_name, **attributes):
	attribute_list = [
		f'{name}={value}'
		for name, value in attributes.items()
	]
	return f"<{tag_name} {' '.join(attribute_list)}>"

my_tag = tag('a', href="http://treyhunner.com")
# print(my_tag)

#🛠 Asterisks
# Positional arguments
def save_ranking(*args):
  print(args)
# save_ranking('ming', 'alice', 'tom', 'wilson', 'roy')

# Keyword arguments
def create_user(**data):
	print(type(data))
	print(data)

# create_user(email='test@test.com', name='Test')

# Both positional and keyword arguments
def create_user(email, password=None, **extra_data):
	print('Creating user:', email, password, extra_data)

user_data = {'name': 'Test', 'age': 30}
# Asterisk ** is used for "packing" user_data arguments
# create_user('test@test.com', 'password', **user_data)

# Unpacking the container
headers = {
	'Accept': 'text/plain',
	'Content-Length': 348,
	'Host': 'https://test.com'
}

def pre_process(**headers):
	#🛠 Unpacking
	content_length = headers['Content-Length']
	print(headers)
	print('content length: ', content_length)
	host = headers['Host']
	if 'https' not in host:
		raise ValueError('You must use SSL for http communication')

#🛠 Packing
pre_process(**headers)