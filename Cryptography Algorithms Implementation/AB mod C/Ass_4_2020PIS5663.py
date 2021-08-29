"""
An algorithm and write program to calculate A^B mod C quickly.
Two cases can be considered:
If B is a power of 2
If B is not a power of 2

This program is written using Python Version 3.

Note : TO MODIFY THE VALUE OF A,B,C PLEASE CHANGE IT IN THE "input.txt" FILE
________________________________________________________________________________

"""

#TO MODIFY THE VALUE OF A,B,C PLEASE CHANGE IT IN THE "input.txt" FILE

content = open("input.txt","r") #opening input fie to get the value of A,B and C
input_str = content.read() #copying the content of the input.txt into a variable
input_list = input_str.split(" ") #change the input_str string to a list split by a space
print("Input value of A,B,C are : {}".format(input_list)) #printing the value of A,B,C 

#TO MODIFY THE VALUE OF A,B,C PLEASE CHANGE IT IN THE "input.txt" FILE
a = int(input_list[0]) #adds the value of A as integer
b = int(input_list[1]) #adds the value of B as integer
c = int(input_list[2]) #adds the value of C as integer

#computes A^B MOD C for B is a power of 2
def compute_b_pow_2(a,b,c):
	print("B is a power of 2")

	b_val = 1 #variable to hold the value of b
	ans = 1 #variable to hold the value of A^B MOD C 
	ans = pow(a,b_val)%c #computing A mod C

	#a loop to compute A^B mod C
	while b_val != b:
		ans = (ans * ans)%c #using prev value of A^2^x mod C
		b_val = b_val *2 #incrementing b_val by factor of 2
	return ans

#computes A^B MOD C for B is not a power of 2
def compute_b_not_pow_2(a,binary_b,c):
	print("B is not a power of 2")
	binary_b.reverse() #reverse the list for computation purpose
	new_list = [] #a list to hold the corresponding values of A^2^i 

	# a loop to calculate A^2^i
	for i in range(len(binary_b)):
		if(binary_b[i] == 1):
			temp = pow(a,pow(2,i))
			new_list.append(temp)
		else:
			new_list.append(binary_b[i])

	new_list_2 = [] #a list to hold the corresponding values of (A^2^i)mod C

	# a loop to calculate (A^2^i)mod C
	for i in range(len(binary_b)):
		temp = new_list[i]%c
		new_list_2.append(temp)
	
	mul = 1 #a variable to hold the product of all non-zero elements of new_list_2
	
	# a loop to find the product of all non-zero elements of new_list_2
	for i in new_list_2:
		if(i != 0):
			mul = mul*i
	
	ans = mul%c # calculating the final value of A^B mod C
	return ans


#converts the B into its binary value
binary_b = [int(i) for i in bin(b)[2:]]
print("Binary form of B : {}".format(binary_b))

count = 0

#counts the number of 1 in the binary form of b 
for i in binary_b:
	if(i == 1):
		count = count +1

#if count = 1 and first letter is 1 then b is power of 2 else not
if(binary_b[0] == 1 and count == 1):
	#for B is a power of 2
	result = compute_b_pow_2(a,b,c)
else:
	#for B is not a power of 2
	result = compute_b_not_pow_2(a,binary_b,c)

print("Result : {}".format(result))

output_num = open("output.txt","w+") # creates a new file output.txt and opens with read,write permission
output_num.write(str(result)) #writes the value of result in output.txt
output_num.close() #closes the file output.txt
content.close() #closes the file input.txt