

# 1.  Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
"""
def below_mean(l):
    sum = 0
    mean = 0
    below_mean = []
    for i in range(0,len(l)):
        sum += l[i]
    mean = sum / len(l)
    for i in range(0,len(l)):
        if l[i] < mean:
            below_mean.append(l[i])
    if len(below_mean) != 0:
        return below_mean

print(below_mean([1, 3, 5, 6, 4, 10, 2, 3]))

"""

# 2. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

"""
def two_lowest_elements(l):
    lowest1, lowest2 = l[0], l[1]
    lowest1_index = 0
    if len(l) == 2:
        return str(lowest1) + ", " + str(lowest2)
    if len(l) <= 1:
        return "List should consist of at least 2 elements"
    for i in l:
        if i <= lowest1:
            lowest1 = i
    lowest1_index = l.index(lowest1)
    l.remove(lowest1)
    if lowest1_index < len(l):
        lowest2 = l[lowest1_index]
    else:
        lowest2 = l[lowest1_index - 1]
    for i in l:
        if i <= lowest2:
            lowest2 = i
    l.insert(lowest1_index, lowest1)
    return str(lowest1) + ", " + str(lowest2)

print(two_lowest_elements([198, 3, 4, 9, 10, 9, 2]))
"""

