"""
A python script to perform Miller-Rabin Primality Test and find the strong 
pseudo primes base 2 up to 10^5.

NOTE : A python package "sympy" is used so please install the package.
	   Steps to import the package : 1. Open command prompt or terminal
	   								 2. run "pip install sympy"

This program is written using Python Version 3
________________________________________________________________________________

"""
import random 
import sympy

lower = 2 #first number to be tested for prime
upper = pow(10,5) #last number to be tested for prime ie 10^5
k = 4 #number of iteration to be performed

prime_list = sympy.primerange(lower,upper) # a list of all prime betn 3 and 10^5

prime_set = set() # a set to hold all primes

#adding all prime to a set
for i in prime_list:
	prime_set.add(i)
 
# a function to cal (x^y) % p 
def power(x, y, p): 
	
	res = 1; # variable to store (x^y) % p 
	
	# Update x if it is more than or 
	# equal to p 
	x = x % p; 
	while (y > 0): 
		
		# If y is odd, multiply 
		# x with result 
		if (y & 1): 
			res = (res * x) % p; #mod operation to keep x in range of p
		y = y>>1; # y = y/2 
		x = (x * x) % p; #mod operation to keep x in range of p
	
	return res; 

#a functio which compute the algo of Raben Miller Test
def millerTest(d, n): 
	
	a = 2; # base

	# Compute a^d % n 
	x = power(a, d, n); 

	# if x is 1 or n-1 ie -1 return true
	if (x == 1 or x == n - 1): 
		return True; 

	# Iterating
	# (i) d does not reach n-1 
	# (ii) (x^2) % n is not 1 
	# (iii) (x^2) % n is not n-1 
	while (d != n - 1): 
		x = (x * x) % n; 
		d *= 2; 

		if (x == 1):
			#if x = 1 the n is composite prime 
			return False; 
		if (x == n - 1): 
			#if x = n-1 ie -1 then n is probable prime
			return True; 

	# Return composite 
	return False; 

# It returns false if n is composite and returns true if n is probably prime.  
def isPrime( n, k): 
	
	# bottleneck cases 
	if (n <= 1 or n == 4): 
		return False; 
	if (n <= 3): 
		return True; 

	# Find r such that n = 2^d * r + 1 for some r >= 1 
	d = n - 1; 
	while (d % 2 == 0): 
		d //= 2; 

	# Iterate given nber of 'k' times 
	for i in range(k): 
		if (millerTest(d, n) == False): 
			return False; 

	return True; 

# Number of iterations for accuracy
k = 4; 

miller_primes = set()

# Checking all number for probable prime by Rabin Miller Test
for n in range(1,100000): 
	if (isPrime(n, k)): 
		miller_primes.add(n)

#Set subtraction betn miller's primes and real primes
pseudoprimes = miller_primes - prime_set

print("PSEUDOPRIMES : {}".format(pseudoprimes))
