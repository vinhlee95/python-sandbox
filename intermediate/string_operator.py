"""
String operators
"""
# 🛠 Convert between list and string
names = 'Ron, Harry, Hermione'
name_list = names.split(',')
original_name_string = ','.join(name_list)
dashed_name_list = ' -'.join(name_list)
print(original_name_string)
print(dashed_name_list)

# 🛠 Convert between numbers and strings
my_string = str(100)
print(my_string, type(my_string))

float_string = 3.14
print(float(float_string))