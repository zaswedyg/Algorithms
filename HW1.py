



# 1. Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
#  Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

"""def compute_sum(n):

    sum = 0
    i = 1
    for i in range(n+1):
        sum += i
    return print(sum)

num = int(input("Enter the number:"))
compute_sum(num)
"""

# 2. Find max number from 3 values, entered manually from a keyboard.
#   Example: 124, 21, 32. Result = 124.

"""def find_max(a,b,c):
    if a>=b and a>=c:
            return a
    if b>=a and b>=c:
        return b
    if c>=a and c>=b:
        return c

value1 = int(input("Enter first value:"))
value2 = int(input("Enter second value:"))
value3 = int(input("Enter third value:"))

print(find_max(value1,value2,value3))
"""

# 3. Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


"""def odd_even(number):
    odds = 0
    evens = 0

    while number != 0:
        current_digit = number % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1
        number = number // 10

    return ["Evens: " + str(evens), "Odds: " + str(odds)]

num = int(input("Enter number:"))
print(odd_even(num))
"""