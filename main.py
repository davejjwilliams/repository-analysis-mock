from maths import *
from conversions import *

num = 5

print ("Maths:")
print("Factorial of {} = {}".format(num, fact(num)))
print("Square of {} = {}".format(num, sq(num)))
print("{} is even? {}".format(num, even(num)))
print("{} is odd? {}".format(num, odd(num)))
print()
print("Conversions:")
print("{} kilometres is {} metres".format(num, km_to_m(num)))
print("{} miles is {} kilometres".format(num, miles_to_km(num)))
print("{} inches is {} centimetres".format(num, in_to_cm(num)))