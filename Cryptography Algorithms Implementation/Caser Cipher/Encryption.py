"""
NOTE : In this program symbols such as comma(,),fullstop(.),spaces and newline are keep unchanged and remain uncoded as c.

This program is written using Python Version 3
________________________________________________________________________________

"""

original_msg = open("input.txt",'r') #opening the input file
content = original_msg.read() #reading the input file and storing the content of the file in a variable
print(content)

my_key = open("key.txt",'r') #opening the kep file
my_shift = my_key.read() #reading the key file and storing the content of the file in a variable
shift = int(my_shift) #converting the content of the input file which is a string into integer

#encryption function which returns the cipher text                 
def encrypt(content,shift): 
    cipher = ""  #variable to store the cipher text.
    for i in range(len(content)): #a loop to encrypt the plain text.
        char = content[i] #the variable which stores the alphabet to be encrypted.
        
        if(char.isupper()):
        	#encryption formula for capital alphabets. 
            cipher += chr((ord(char) + shift - 65 ) % 26 + 65 )
        elif(char == "\n"):
        	#code to keep new line as it is.
            cipher += "\n"
        elif(char == "." or char == "," or char == " "):
        	#code to keep fullstops,commas and spaces as it is.
            cipher += char
        else:
        	#encryption formula for small alphabets
            cipher += chr((ord(char) + shift -97) %26 + 97)
    return cipher


result = encrypt(content,shift) #variable to store the returned cipher text
print(result)

cipher = open("output.txt","w+") #creates a text file call output
cipher.write(result) #writes the cipher text to the file "output"
cipher.close() #closing the cipher file ie output.text
original_msg.close() #closing the plain text file ie input.txt
my_key.close() #closing the key file ie key.txt

