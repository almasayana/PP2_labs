import math
def volume_s(radius):
    return radius ** 3 * 4/3 * math.pi
r = int(input())
print(volume_s(r))