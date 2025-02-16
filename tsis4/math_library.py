import math
#1
degree = int(input("Input degree: "))
print(f"Output radian: {degree * math.pi / 180:.6f}")
print()

#2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print("Expected Output:", (a+b)*h/2)
print()

#3
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area:.1f}")
print()

#4
a = int(input('Length of base: '))
b = int(input('Height of parallelogram: '))
print(f"Expected Output: {a*b:.1f}")