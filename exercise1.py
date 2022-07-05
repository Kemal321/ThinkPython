#Exercise 1.1
print("Hello, world!")
"""
We get a syntax error when we leave one or both paranthesis mark 
SyntaxError: '(' was never closed or unmatched acc to positon of paranthesis or missing paranthesis in call to 'print'. Did you mean print(..)?
"""

# Exercise 1.2
print("Hello, world!")
"""
Same we take some syntax error when we leave one or both quotation marks.

"""
# Exercise 1.3

"""
You can use a minus sign to make a negative number like -2. What happens if you put a plus
sign before a number? What about 2++2?
--When we try to make 2++2 operation in terminal gives an error unexpected token 
"""
# Exercise 1.4
#I take an error about leading zeros in this exercise
#Leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a = 0o33
print(int(a))

# Exercise 1.5
a =3 
b = 5 
print(a+b)
# there is no action in program because proram does not identify ab 

# Exercise 2.1
# 1. How many seconds are there in 42 minutes 42 seconds?
# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
# mile in minutes and seconds)? What is your average speed in miles per hour?

min = 42
sec = 42
totalSeconds=min*60+sec
print("There are",totalSeconds," second in 42 minutes and 42 seconds")
perMile=1.61
totalKm=10
totalMile=totalKm/perMile
print("There",totalMile," in 10 km.")

print("Average pace time per mile in minutes and seconds ",totalMile/totalSeconds," mil/sec ",totalMile/(42+42/60)," mil/min")