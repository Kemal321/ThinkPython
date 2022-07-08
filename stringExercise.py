##FIRST EXERCISE

def countinvoke(letter,target):
    count=0
    for i in target:
        if letter==i:
            count +=1
    return count
print(countinvoke('a','banana'))

## SECOND EXERCISE

def is_palindrome2(target,mirror):
    target2=target[::-1]
    if target2==mirror:
        print("Excellent you find a palindrome pair.")
    else:
        print(target2,mirror,"are not palindrome pair try again.")
is_palindrome2("stop","pots")

## THIRD EXERCISE 

# any_islowercase3 function return a boolean value the last letter lowercase or not 
def any_islowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
print(any_islowercase3("şsldkjflkşfjsgldfsjF"))


## FOURTH EXERCISE 

def rotate_word(what,how):
    answer=""
    for i in what:
        yeni=chr((ord(i)-how))
        answer = answer+yeni
    return answer 
print(rotate_word("hal",-1))


