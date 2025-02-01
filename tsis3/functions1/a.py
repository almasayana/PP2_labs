def convert_to_ounces(x):
    return x / 28.3495231 

grams = float(input("Enter the number of grams: "))
print('You need', f'{convert_to_ounces(grams):.3f}', 'ounces')

