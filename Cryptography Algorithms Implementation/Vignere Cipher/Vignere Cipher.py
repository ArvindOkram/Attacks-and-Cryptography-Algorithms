""" 
Implemention of Vigenere polyalphabetic cipher for messages composed from the
letters of the English alphabets (well written comments should be there). 
Submit the following files
1. Program
2. input.txt
3. key.txt
4. output.txt

This program is written using Python Version 3
_________________________________________________________________________________
"""
import math #import math package

#OPENING FILE TO GET PLAINTEXT AND KEY
text_open = open("input.txt","r") #open input.txt
plain_text = text_open.read() # copys the plaintext to our variable
print("Plain Text : {}".format(plain_text))
key_open = open("key.txt","r") #open key.txt
key = key_open.read() #copys the key to our variable
print("\nKey : {}".format(key))


#STEP 1 : GETTING THE NUMERIC VALUE OF PLAINTEXT AND KEY

plain_text_list = [] #list to stores the numeric value of alphabet in plaintext
key_list = [] #list to stores the numeric value of alphabet in key
#convert plaintext to each numeric value and append it into a new list
def plain_text_to_integer(plain_text):
	for i in range(len(plain_text)):
		char = plain_text[i]
		if(char.isupper()):
			temp = int((ord(char) - 65 ))
			plain_text_list.append(temp)
		if(char.islower()):
			temp = int((ord(char) - 97))
			plain_text_list.append(temp)

#convert key to each numeric value and append it into a new list
def key_to_integer(key):
	for i in range(len(key)):
		char = key[i]
		if(char.isupper()):
			temp = int((ord(char) - 65 ))
			key_list.append(temp)
		if(char.islower()):
			temp = int((ord(char) - 97))
			key_list.append(temp)

plain_text_to_integer(plain_text) #function call
key_to_integer(key) #function call


#STEP 2 : MAKING THE KEY SUFFICIENTLY LONG TO ENCRYPT THE WHOLE PLAIN TEXT

key_wrap_around = [] # a list to hold the wrap key 
plain_text_length = len(plain_text_list) #calcutating plaintext length
key_length = len(key_list) #calculationg key length
factor = math.floor(plain_text_length/key_length) #calculating who much times the keylength should be to encrypt the plaintext
#appending the key so that we get a key wrap to encrypt the whole plaintext
while (factor+1) > 0:
	key_wrap_around.extend(key_list)
	factor = factor-1


#STEP 3 : CALCULATING THE NUMERIC VALUE OF CIPHER TEXT

cipher_num = [] # a list to hold the numeric value of cipher text
#calculating numeric value of cipher text
for i in range(plain_text_length):
	temp = (plain_text_list[i] + key_wrap_around[i])%26
	cipher_num.append(temp)

#STEP 4 : GETTING THE CORRESPONDING ALPHABET FOR THE CIPHER NUMERIC VALUE

#a function to convert numeric cipher value to each corresponding alphabet
def cipher_num_to_cipher_text(cipher_num):
	cipher_list = []
	for i in range(len(cipher_num)):
		temp = chr(cipher_num[i]+65)
		cipher_list.append(temp)
	listToStr = ' '.join(map(str, cipher_list))
	return listToStr
#gets the return cipher text from the function cipher_num_to_cipher_text
cipher_result = cipher_num_to_cipher_text(cipher_num)
print("\nCipher : {}".format(cipher_result))
#creating a file to store the cipher text output.text
cipher = open("output.txt","w+")
cipher.write(cipher_result) #writes the cipher text into the file output.txt

#CLOSING ALL OPENED FILES
cipher.close() #closes the file output.txt
text_open.close() #closes the file input.txt
key_open.close() #closes the file key6.txt
