

#  1. Reverse a Statement
#Build an algorithm that will print the given statement in reverse.
#Example: Initial string = Everything is hard before it is easy
#Reversed string = easy is it before hard is Everything
"""
def reverse_statement(s):
    list = s.split()
    list.reverse()
    return " ".join(list)

print(reverse_statement("Everything is hard before it is easy"))
"""


# 3.  Count Characters
#Create a program that will count vowels and consonants in a string.
#Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

"""
def count_characters(s):
    vowels = 0
    consonants = 0
    spaces = 0
    for i in s:
        if "a" in i or "e" in i or "u" in i or "i" in i or "o" in i or "A" in i or "E" in i or "U" in i or "I" in i or "O" in i:
            vowels += 1
        elif " " in i:
            spaces += 1
        else: consonants += 1
    return "{Vowels : " + str(vowels) + " Consonants: " + str(consonants) + "}"

print(count_characters("hello world"))
"""