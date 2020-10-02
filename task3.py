#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
number=input("Enter number")
number=float(number)
a=str(number)
b=0
if number < b:
    print(""+a+" "+"is not a positive integer")
else:
    print(""+a+" "+"is a positive integer")
