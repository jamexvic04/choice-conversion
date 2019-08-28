def ispalindrome():  
    a_str = str(input("enter any word:"))
    a_str = a_str.casefold()#to make it suitable for caseless comparison
    rev_str = reversed(a_str)#to reverse string
# to check if the str is = to its reversed
    if list(a_str) == list(rev_str):
        
        print("it is a palindrome")
    else:
        print("it is not a palindrome")#A program to check if a string entered by a user is a (palindrome or not)
ispalindrome()