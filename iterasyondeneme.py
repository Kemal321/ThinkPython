import math
def mysqrt(a):
    """Calculates square root using Newton's method:
    https://en.wikipedia.org/wiki/Newton's_method
    
    a - positive integer < 0;
    x - estimated value, in this case a/2
    """
    x = a/2
    while True:
        estimated_root = (x + a/x) / 2
        if estimated_root == x:
            return estimated_root
            break
        x = estimated_root
        print(a,estimated_root,math.sqrt(a))
mysqrt(range(1,10))