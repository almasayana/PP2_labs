from l import histogram
from f import reverse_sentence
from i import volume_s
h1 = histogram([1, 2, 2, 1])

s = input("Enter a sentence: ")
print(reverse_sentence(s))

r = int(input("Enter the radius: "))
print("The volume is ", volume_s(r))