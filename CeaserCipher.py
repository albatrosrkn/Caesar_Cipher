# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:40:06 2021

@author: Kullanıcı
"""

import string 
alphabet=string.ascii_lowercase+string.ascii_uppercase
key=6
def choice():
    Input=input("E or D:").lower()
    if Input=="e":
        encrypt()
    elif Input=="d":
        decrypt()
    else:
        print("Invalid input")
def encrypt():
    text=input("Please Enter a message:")
    result=' '
    newMessage=""
    for i in text:
        position=alphabet.find(i)
        newPosition=(position+key)%26
        Newch=alphabet[newPosition]
        newMessage+=Newch
    print("Your message is :",newMessage)
def decrypt():
    ciptext=input("Please enter encrypte message: ")
    newMessage=""
    for i in ciptext:
        position=alphabet.find(i)
        newPosition=(position-key)%26
        Newch=alphabet[newPosition]
        newMessage+=Newch
    print("your message is :",newMessage)
    
choice()
    