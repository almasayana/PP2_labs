def solve():
    numheads = int(input("Enter the number of heads: "))
    numlegs = int(input("Enter the number of legs: "))
    
    x = (4 * numheads - numlegs) // 2
    y = numheads - x
    
    if x < 0 or y < 0 or (2*x + 4*y != numlegs):
        return "No valid solution"
    
    print(f"Chickens: {x}, Rabbits: {y}")

solve()

