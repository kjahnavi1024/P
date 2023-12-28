#Python Numeric Data Types
# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# boolean variable.
b=True
print("The type of variable having value", b, " is ", type(b))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))

#Python Sequence Data Type
#String Data Type
str = 'Welcome to Maang'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 3)      # Prints string three times
print (str +" " + "Jahnavi") # Prints concatenated string

#Python List Data Type
list = [ 'jahnavi', 9876543210 , 2.23, 'janu', 70.2 ]
tinylist = [12345, 'maang']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

#Python Tuple Data Type
tuple = ( 'kummari', 786 , 2.23, 'jahnavi', 987654321  )
nexttuple = (13, 'anu',45.08)

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (nexttuple * 2)       # Prints the contents of the tuple twice
print (tuple + nexttuple)   # Prints concatenated tuples

#Python Ranges Function
for i in range(10):
  print(i)

for i in range(1, 25):
  print(i)

for i in range(1, 25, 12):
  print(i)


#Python Dictionary Data Type
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'jahnavi','id':9012, 'domain': 'fullstack'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

#Python Boolean Data Types
a = True
# display the value of a
print(a)

# display the data type of a
print(type(a))


# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns false as a is 10
a = 10
print(bool(a))

  
