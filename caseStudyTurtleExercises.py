import turtle
bob = turtle.Turtle()
def square(t,length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
square(t=0,length=200)
