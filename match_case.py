#Python - Match-Case Statement
# Example usage
def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))

#combined cases
def classify_day(n):
    match n:
        # Combined cases for weekdays (0 to 4)
        case 0 | 1 | 2 | 3 | 4:
            return "Weekday"
        
        # Combined cases for weekends (5 to 6)
        case 5 | 6:
            return "Weekend"

        # Default case for invalid day number
        case _:
            return "Invalid day number"

# Example usage
print(classify_day(3)) 
print(classify_day(6)) 
print(classify_day(7))

#Using "if" in "Case" Clause

def calculate_interest(details):
    match details:
        case [amt, duration] if amt < 10000:
            return amt * 10 * duration / 100
        case [amt, duration] if amt >= 10000:
            return amt * 15 * duration / 100
        case _:
            return "Invalid input"

# Example usage
print("Interest =", calculate_interest([90000, 15]))
print("Interest =", calculate_interest([15000, 3]))

