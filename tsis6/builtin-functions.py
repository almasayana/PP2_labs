from functools import reduce 
from operator import mul
import math
import time

#1
def mult(arr):
    return reduce(mul, arr) 

arr = list(map(int, input().split()))
print(mult(arr))


#2
def check(s):
    upper = len(list(filter(str.isupper, s))) 
    lower = len(list(filter(str.islower, s)))

    print(f"Count of upper case: {upper}")
    print(f"Count of lower case: {lower}")

s = input()
check(s)


#3
def is_palindrome(s):
    return s == ''.join(reversed(s)) 

s = input()
if is_palindrome(s): print("Yes, it is")
else: print("No, it is not")


#4
def sqrt(n):
    return math.sqrt(n)

n = int(input())
ms = int(input())

time.sleep(ms / 1000)

result = sqrt(n)
print(f"Square root of {n} after {ms} milliseconds is {result}")


#5
tup = (1, 0, 1, 0, 1)
print(all(tup))