import turtle
polygon = turtle.Turtle()
def square(n,length):
    for i in range(n):
        polygon.fd(length)
        polygon.lt(360/n)
square(n=6,length=200)
turtle.mainloop()
