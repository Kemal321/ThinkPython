from cmath import pi
from turtle import done


import math
def eval_loop():
    while True:
        inp=input('>>')
        if  inp != "done":
            print(eval(inp))
        else:
            break
def factorial(n):
    if n == 0 :
        return 1 
    else:
        return n*factorial(n-1) 
def estimate_pi():
    """Computes an estimate of pi.
    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """
    sum=0
    k=0
    suf=(2*math.sqrt(2))/9801
    while True:  
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        
        sum += num / den
        term = suf * num/den
        
        if abs(term) < 1e-15:
            break
        k += 1

    return 1/(suf*sum)
print(estimate_pi())
