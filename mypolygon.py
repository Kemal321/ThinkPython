from re import X
import turtle
bob = turtle.Turtle()
print(bob)
"""
bob.fd(100)
bob.lt(90)s
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
"""
x=1000
for i in range(10):
    bob.fd(x/2)
    bob.lt(90)
    x=x/2

turtle.mainloop()

