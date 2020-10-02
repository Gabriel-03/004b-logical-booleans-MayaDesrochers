"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3

number=input("Enter number")
number=float(number)
a=str(number)
if (number%6==0 and number%8==0):
    print(""+a+" "+"is not frue")

elif (number%6==0 and number%8>0):
    print(""+a+" "+"is frue")
