def is_palindrome(s):
    print(s==s[::-1])

s = input("Enter a word or phrase: ").replace(" ", "").lower()       
is_palindrome(s)
    
        
    