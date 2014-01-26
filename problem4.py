# 999 * 999 = 998001
import math

def is_palindrome(num):
    string = str(num)
    length = len(string)
    for i in range(length/2):
        if string[i] != string[(length - 1) - i]:
            return False
    return True
    
def largest_palindrome_less_than_998001():
    i = 998001
    while True:
        if is_palindrome(i):
            return i
        i -= 1

print largest_palindrome_less_than_998001()