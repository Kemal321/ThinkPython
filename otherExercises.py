
# 1. WORKSHOP
## Change the values of x and y and print them to out
x = 10 
y = 20 

print("x = "+ str(x))
print("y = "+ str(y))

# 1.way
x , y = y, x 

print("x = "+ str(x))
print("y = "+ str(y))

print("*******************************\nTrue****************")

# 2.way
x = 10 
y = 20 

print("x = "+ str(x))
print("y = "+ str(y))

temp = x 
x = y 
y = temp 

print("x = "+ str(x))
print("y = "+ str(y))

# EXERCISE PYTHON MUTATION
def mutate_string(string, position, character):
    new_string = string[:position]+character+string[(position+1):]
    return new_string
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# EXERCISE DESIGNER DOOR MAT

N,M = input("").split()
N=int(N)
M=int(M)
i,b=1,1
design1 = ".|."
design2 = "---"
while i<= N-(N//2):
    if i == N-(N//2):
        print("-"*((M-7)//2)+"WELCOME"+"-"*((M-7)//2))
        b +=2
        i +=1
        break 
    print(design2*int((M/6)-(b/2))+design1*b+design2*int((M/6)-(b/2)))
    b +=2
    i +=1 
i2=1
b2=(M-6)//3
while i2< N-N//2:
    print(design2*i2+design1*b2+design2*i2)
    i2 +=1
    b2 -=2