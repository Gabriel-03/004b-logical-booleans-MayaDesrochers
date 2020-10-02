#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
a=input("Enter an integer")
b=input("Enter an integer")
c=input("Enter an integer")
a=int(a)
b=int(b)
c=int(c)
if (a<b and a<c) and b<c:
    x=a 
    y=b
    z=c
elif (b<a and b<c) and a>c:
    x=b
    y=c
    z=a
elif (a>b and a<c) and b<c:
    x=b
    y=a
    z=c
elif (a<b and a>c) and b>c:
    x=c
    y=a
    z=b
elif (a>b and a>c) and b>c:
    x=c
    y=b
    z=a
elif (a<b and a<c) and b>c:
    x=a
    y=c
    z=b
    
smallest=str(x)
middle=str(y)
largest=str(z)

if x**2+y**2==z**2:
    print(""+smallest+","+middle+","+largest+" " +"form a Pythagorean triple")
else:
    print(""+smallest+","+middle+","+largest+" " +"do not form a Pythagorean triple")
