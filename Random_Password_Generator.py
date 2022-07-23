#@smdetroja all rights reserved
#importing random library 
import random

#importing library for saving path
import os.path

myApp = input("Enter parent name of password (Add name of existing file where you want to update the password): ")

#defining characters for password
lower = "qwertyuioplkjhgfdsazxcvbnm"
upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
number = "0123456789"
symbols = "!@#$%^&*)("

#making password using defined characters 
string = lower + upper + number + symbols

# length of password
lenght = 16
password = "".join(random.sample(string,lenght))

#printing password 
print("Your new password: ",password)

#giving path to for saving file in computer 
save_path = 'C:\Password'

#creating file name and giving path
complete_Name = os.path.join(save_path, myApp+".txt") 

#Opens or creates the .txt file, sharing the directory of the script#
text_file = open(completeName, "w")

#Writes the variable into the .txt file#
text_file.write(myApp+"\nPassword: "+password)

#Closes the .txt file#
text_file.close()
