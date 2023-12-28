# Example of a simple while loop
count = 0
while count < 5:
    count += 1
    print("Iteration no. {}".format(count))

print("End of while loop")

# Example of an infinite while loop with user input
var = 1
while var == 1:  # This constructs an infinite loop
    num = int(input("Enter a number: 10"))
    print("You entered:", num)

print("Good bye!")

# Example of a while-else loop
count = 0
while count < 5:
    count += 1
    print("Iteration no. {}".format(count))
else:
    print("While loop over. Now in else block")

print("End of while loop")
