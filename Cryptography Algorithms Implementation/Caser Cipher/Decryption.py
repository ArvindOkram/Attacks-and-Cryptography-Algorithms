"""
Breaking a Caser Cipher and recovering both the original message and the encryption 
key used by mounting a brute-force attack on the encryption/decryption algorithms. 

PREREQUISITE FOR THE PROGRAM : Please install langdetect package to detect whether 
							   the generated plain text is English language
INSTALLING LANGDETECT : In command prompt please run the command "pip install langdetect" 

NOTE: This program undergoes brute-force attack

This program is written using Python Version 3
________________________________________________________________________________

"""
from langdetect import detect #importing langdetect package

cipher_text = "efgfoe uif fbtu xbmm pg uif dbtumf" #a cipher text

key = 0 #intializing the value of key as 0

#a loop to undergo brute force attack
while(key<26):
	plain_text = "" #variable to store the plain text
	for i in range(len(cipher_text)): 
		content = cipher_text[i] #stores single alphabet to be decrypted

		if(content.isupper()):
			#decryption formula for capital alphabets.
			plain_text += chr((ord(content) - key - 65 ) % 26 + 65 )
		elif(content == "\n"):
			#code to keep new line as it is.
			plain_text += "\n"
		elif(content == "." or content == "," or content == " "):
			#code to keep fullstops,commas and spaces as it is.
			plain_text += content
		else:
			#decryption formula for small alphabets.
			plain_text += chr((ord(content) - key -97) %26 + 97)
	
	language = detect(plain_text) #detect the language of the plain text
	
	#conditional statement to check whether the decrypted plain text is English language
	if(language == 'en'):
		#prints key and plaintext if the language of the plain text is English
		print("key : ",key)
		print("\n")
		print(plain_text)
		break

	key += 1 #incrementing key for the next brute force attack

