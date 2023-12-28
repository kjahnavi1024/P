# Explicit Typecasting Examples

# Converting an integer
a = 10
print("a:", a)
print("Type of a:", type(a))

# Converting a float to an integer
a = int(10.5)
print("a:", a)

# Converting a float expression to an integer
a = int(2 * 3.14)
print("a:", a)
print("Type of a:", type(a))

# Converting a boolean to an integer
a = int(True)
print("a:", a)
print("Type of a:", type(a))

# Converting a string to an integer
a = int("100")
print("a:", a)
print("Type of a:", type(a))

# Concatenating strings and converting to an integer
a = int("10" + "01")
print("a:", a)
print("Type of a:", type(a))

# Converting a binary string to an integer
a = int("110011", 2)
print("a:", a)

# Converting an octal string to an integer
a = int("20", 8)
print("a:", a)

# Converting a hexadecimal string to an integer
a = int("2A9", 16)
print("a:", a)

# Converting an integer to a float
a = float(100)
print("a:", a)
print("Type of a:", type(a))

# Converting between different iterable objects
a = [1, 2, 3, 4, 5]   # List Object
b = (1, 2, 3, 4, 5)   # Tuple Object
c = "Hello"           # String Object

# Converting list to other types
obj = list(c)
print("List from string:", obj)

obj = list(b)
print("List from tuple:", obj)

obj = str(a)
print("String from list:", obj)

# Converting tuple to other types
obj = tuple(c)
print("Tuple from string:", obj)

obj = tuple(a)
print("Tuple from list:", obj)

obj = str(b)
print("String from tuple:", obj)
