#1
def sq_generator(n):
    for i in range(n + 1):
        yield i ** 2

print(f"The squares of numbers:")
for num in sq_generator(4):
    print(num, end=" ")
print('\n')


#2
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(f"Even numbers between 0 and {n}:")
print(", ".join(map(str, even_generator(n))))
print()


#3
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
print(f"Numbers which are divisible by 3 and 4, between a given range 0 and {n}:")
print(list(div_by_3_and_4(n)))
print()


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print("the square of all numbers between a given range:")
for num in squares(7, 15):
    print(num, end=" ")
print('\n')


#5
def rev(n):
    for i in range(n, -1, -1):
        yield i

print('Numbers from a given N down to 0:')
for num in rev(6):
    print(num, end=" ")
