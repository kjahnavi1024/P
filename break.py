#Break statement
# Example 1: Using break in a for loop
for letter in 'Python':
    if letter == 'h':
        break
    print('Current Letter:', letter)

# Example 2: Using break in a while loop
var = 10
while var > 0:
    print('Current variable value:', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")
