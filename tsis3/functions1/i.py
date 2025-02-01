import math
def volume_s(radius):
    return radius ** 3 * 4/3 * math.pi

if __name__ == "__main__":
    r = int(input("Enter the radius: "))
    print("The volume is ", volume_s(r))