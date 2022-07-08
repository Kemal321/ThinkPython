"""
I will try to debug on exercise of chapter 10 
"""
def is_reverse(word1, word2):
    if len(word1) != len(word2):
         return False
    i = 0
    j = len(word2)
    while j > 0:
        print("Test Case",i,j)
        if word1[i] != word2[j-1]:
            return False
        i = i+1
        j = j-1
    return True
print(is_reverse("Kemal","lameK"))