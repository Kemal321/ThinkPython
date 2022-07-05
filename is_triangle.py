a=int(input("Enter the length of first edge: "))
b=int(input("Enter the length of first edge: "))
c=int(input("Enter the length of first edge: "))
def is_triangle(a,b,c):
    """
    This function check given 3 length of stick that They can be used for making a triangle.
    """
    if a+b>c and a+c>b and c+b>a:
        print("Yes")
    elif a+b ==c or a+c ==b or c+b==a:
        print("Yes")
    else:
        print("No")
     
#Example for fruitful functions
def compare(x,y):
    if x<y:
        return -1
    elif x==y:
        return 0
    else:
        return 1
print(compare(3,5))

# Boolean function
def is_between(x,y,z):
    return (x<=y<=z) ==1
       
print(is_between(2,3,4))
print(is_between(5,3,4))


