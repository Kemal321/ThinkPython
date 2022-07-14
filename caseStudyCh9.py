from distutils.command.build_scripts import first_line_re
from itertools import count
from os import fstat


fin = open("words.txt")

for line in fin:
    word=line.strip()
   # print(word)

 #EXERCISE 9.1

def count20():
    defter=open('words.txt')
    a=0
    for kelime in defter:
        ickelime=kelime.strip()
        if len(ickelime) > 19:
            print(ickelime)


# EXERCISE 9.2

def has_no_e(word):
    count = 0
    for i in word:
        if i == 'e':
            count += 1
        else:
            count = count
    if count >0 :
        return False
    else:
        return True


def rewrite_count20():
    defter=open('words.txt')
    a=0
    totalword=0
       
    for kelime in defter:
        ickelime=kelime.strip()
        totalword += 1
        if has_no_e(ickelime):
            print(ickelime)
            a += 1
    print("The percentage of the words are has no e ",a/totalword)   


# EXERCISE 9.3 

def avoids(forbiddenLetters,word):
    fst = forbiddenLetters[0]
    snd = forbiddenLetters[1]
    trd = forbiddenLetters[2]
    frth = forbiddenLetters[3]
    fifth = forbiddenLetters[4]
    for i in word:
        if i != fst | snd | trd | frth | fifth :
            return True 
        else:
            return False 
avoids("abcde", " Krsptüwı")

# EXERCISE 9.4

def uses_only(word,letters):
    defter = open("word.txt")
    for i in word:
        if i != letters:
            return False
        
    