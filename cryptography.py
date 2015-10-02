"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

def efunction (i, m, k):
    letters = list(m)
    r = len(letters)
    letter2 = letters[:]
    print(letters)
    for x in range (0, r):
        p = letters[x]
        l = associations.find(p)
        letter2[x] = l
    print(letter2)
       
       
       
    

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
x = 0
while x == 0:
    i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if i == "e" or i == "d":
        m = input("Message: ")
        k = input("Key: ")
        if i == "e":
            efunction (i, m, k)
        if i == "d":
            dfunction (i, m, k)
    elif i == "q":
        print ("Goodbye!")
        x = 1
    else:
        print ("Did not understand command, try again.")
        print (" ")
    
        