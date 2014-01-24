# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

# prime factor


import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i < math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True

def largest_prime_factor(num):
    i = int(math.sqrt(num))
    print i
    while i > 1:
        if is_prime(i) and num % i == 0:
            return i
        i -= 1
    return None


# for i in range(10):
#     print str(i) + str(is_prime(i))

print largest_prime_factor(600851475143)