#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

a=input("Enter an integer")
b=input("Enter another integer")
a=int(a)
b=int(b)


if a<b:
    x=a 
    y=b
elif a>b:
    x=b 
    y=a
smaller_number=str(x)
larger_number=str(y)

if y%x==0:
    print(""+smaller_number+" "+ "is a factor of"+" "+larger_number+"")
elif y%x==1:
    print(""+smaller_number+" "+ "is not a factor of"+" "+larger_number+"")


