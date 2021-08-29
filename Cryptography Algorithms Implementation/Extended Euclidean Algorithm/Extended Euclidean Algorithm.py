"""
Extended Euclidean Algorithm finds for a,b the integer x and y
such that ax+by=gcd(a,b), and the x is the inverse of a modulo b. 
/* b>1, a is nonnegative */ 
/* a <= b */
Python program and check it  for the input (2613, -2171). Show the output

This program is code in Python Version 3.0
________________________________________________________________________________

"""

num1 = 2613
num2 = -2171

#converting our input value to its absolute
#Since gcd(a,b) = gcd(-a,b) = gcd(a,-b) = gcd(-a,-b)
#So that we get the value of gcd,x and y in its sign actual value
a = abs(num1)
b = abs(num2)

#performing EEA for the 2 input number
def ExtednedEuclidAlgGCD(b,a,x,y):
    #terminating condition of the recursive function
    if b == 0:
        return (a,0,1)
    else:
        #calculating the gcd and updating the intermediate value of x and y
        gcd, x, y = ExtednedEuclidAlgGCD(a%b,b,x,y)
        #return the value of final x and y
        return (gcd,y - (a//b) *x,x)

#parent function for EEA to get inverse of a and b
def inverse(a,b):
    #initializing the value of x and y as 1 and 1
    x,y = 1,1
    #calling EEA for calculating gcd, x and y
    d,x,y = ExtednedEuclidAlgGCD(b,a,x,y)


    if d == 1:
        #if d = 1 ie gcd(a,b) is 1 ie they are co-prime
        print("THE GCD OF {} AND {} IS {} SO THEY ARE CO-PRIME and the value of x and y are {} and {}".format(num1,num2,d,x,y))
    else:
        #if d != 1 ie gcd(a,b) is not 1 ie they are not co-prime
        print("{} and {} are not CO-PRIME as their gcd is {} and value of x and y are {} and {}".format(num1,num2,d,x,y))

#calling the function for our program
inverse(a,b)