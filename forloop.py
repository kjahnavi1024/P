#Python for Loops
#Using "for" with a String
message = 'Keep Calm and Code On'

for char in message:
    if char.isupper():
        print(char, end='')


#Using "for" with a Tuple
# Define a tuple of fruits
fruits_tuple = ('apple', 'banana', 'orange', 'grape', 'kiwi')

# Print the header
print("Fruits:")

# Use a for loop to iterate through each fruit in the tuple
for fruit in fruits_tuple:
    # Print each fruit
    print(fruit)

#Using "for" with a List
numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
   if num%2 == 0:
      print (num)

#Using "for" with a Range Object
for num in range(5):
 print (num, end=' ')
print()
for num in range(10,20):
 print (num, end=' ')
print()
for num in range(1, 10, 2):
 print (num, end=' ')

#Using "for" with Dictionaries
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])
    

