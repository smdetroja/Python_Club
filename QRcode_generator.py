#@smdetroja all rights reserved

#import library 
import pyqrcode
import png
from pyqrcode import QRCode

#getting input from user 
s = input("Enter URL for generating QR : ")

# getting name of the client's QR code 00
name = input("Enter the Name of Company : ")

#generate QR code using libraries 
url = pyqrcode.create(s)
  
url.png(name + ".png", scale = 8)

#it will save where your file has been saved