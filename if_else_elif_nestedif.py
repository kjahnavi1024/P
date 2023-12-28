# If-Else, Elif, Nested If Example

# Example 1: If-Else
age = 25

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 2: Elif
grade = 75

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Example 3: Nested If
num = 10

if num > 0:
    print("Positive number.")
    if num % 2 == 0:
        print("Even number.")
    else:
        print("Odd number.")
elif num == 0:
    print("Zero.")
else:
    print("Negative number.")

