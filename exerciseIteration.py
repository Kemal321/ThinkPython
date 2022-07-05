import math

def mysqrt(x):    
    """while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y"""
    for a in range (1,10):
        y = (x + float(a)/x) / 2
        
        print(float(a),y,"     ",math.sqrt(a),"  ",abs((y-math.sqrt(y))))
        x = y
def test_square_root(x):
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   --------      ------------  ----")
    mysqrt(x)

test_square_root(1)