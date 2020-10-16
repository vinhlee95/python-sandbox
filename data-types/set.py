"""
Set data type

Sets are a datatype that allows you to store other immutable types in an unsorted way.
An item can only be contained in a set once.
There are no duplicates allowed.
The benefits of a set are:
✅ Very fast membership testing along with being able to use powerful set operations, like union, difference, and intersection.

📚 Resources:
https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/50-sets/
https://www.w3schools.com/python/python_sets.asp

"""
# 🛠 Declaration
# name_set = {"Harry", "Rone", "Harry"}
# print(type(name_set), name_set)
# # <class 'set'> {'Harry', 'Rone'}

# 🔑 Set could be use to de-duplicate items in a list
name_list = ["Foo", "Bar", "Foo", "Bar", 1, 2]
name_set = set(name_list)
# print(type(name_set), name_set)
# # <class 'set'> {'Bar', 'Foo'}

# 🛠 Immutable types
# Set cannot store mutable types such as list
# hello_set = {[]}
# TypeError: unhashable type: 'list'

# 🛠 Set does not have an order and items cannot be accessed by position
# print(name_set)
# print(name_set[0])
# TypeError: 'set' object is not subscriptable

# 🛠 Add and remove items
name_set.add("New item")
# print(name_set)
# {1, 2, 'Bar', 'New item', 'Foo'}
name_set.remove("New item")
# print(name_set)
# {1, 2, 'Bar', 'Foo'}

# 🔑 You can update a set by passing in another sequence
# name_set.update({"set 2"})
# name_set.update(["list item 1", "list item 2"])
# name_set.update(("tuple 1", 12))
# print(name_set)

# 🛠 Union
# Create a new set with all items from 2 sets
animal_set = {"Dog", "Cat"}
age_set = {12, 23}
# animal_age = animal_set | age_set
# animal_age = animal_set.union(age_set)
# print(animal_age)

# 🛠 Intersection
# Create a new set containing items that are in BOTH sets
first_class = {"John", "Tom", "Mary"}
second_class = {"John", "Jerry"}
# best_students = first_class & second_class
# best_students = first_class.intersection(second_class)
# print(best_students)

# 🛠 Difference
# Create new set containing items that are NOT in BOTH sets
# separate_students = first_class ^ second_class
# print(separate_students)


