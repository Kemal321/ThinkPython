from operator import is_


def firstword(word):
    return word[0]

def lastword(word):
    return word[-1]

def middleword(word):
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if firstword(word) != lastword(word):
        return False
    return is_palindrome(middleword(word))
a="ekjfdglsfkdg"
print(is_palindrome("kemal"))
print(a[0:])
"""
Anasını satayım yapamadık çok basitti ama yapamadık algoritmayı kafamıza bir kere bile getiremedik.
"""