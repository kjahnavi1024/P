#Continue statement
num = 84
print("Prime factors for:", num)

divisor = 2

while num > 1:
    if num % divisor == 0:
        print(divisor, end=' ')
        num //= divisor
    else:
        divisor += 1
