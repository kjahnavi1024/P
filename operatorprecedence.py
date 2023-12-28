#Python Operators Precedence Example
a = 20
b = 10
c = 10
d = 5
e = 10

e = (a + b) * c / d       #( 30 * 10 ) / 5
print ("Value of (a + b) * c / d is ",  e)

e = ((a + b) * c) / d     # (30 * 10 ) / 5
print ("Value of ((a + b) * c) / d is ",  e)

e = (a + b) * (c / d);    # (30) * (10/5)
print ("Value of (a + b) * (c / d) is ",  e)

e = a + (b * c) / d;      #  20 + (100/5)
print ("Value of a + (b * c) / d is ",  e)
