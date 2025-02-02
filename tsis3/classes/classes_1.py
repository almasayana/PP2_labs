class String:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Enter a string: ")
    
    def printString(self):
        print(self.text.upper())
        
s1 = String()
s1.getString()
s1.printString()