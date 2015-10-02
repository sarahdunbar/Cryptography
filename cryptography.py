"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

def cryptolist(letter2, key2):
    r = len(letter2)
    k = len(key2)
    if r > k:
        range1 = r
        listreal = letter2[:]
    if r < k:
        range1 = k
        listreal = key2[:]
    if r = k:
        range1 = k
        listreal = key2[:]
    for x in range(0, range1):
        if x > r:
            x = x - r - 1
        if x > k:
            x = x - k - 1
        valuem = letter2[x]
        valuen = key2[x]
        valueg = valuem + valuen
        listreal[x] = valueg
    

def efunction (i, m, k):
    letters = list(m)
    letterkey = list(k)
    r = len(letters)
    k = len(letterkey)
    letter2 = letters[:]
    key2 = letterkey[:]
    for x in range (0, r):
        p = letters[x]
        l = associations.find(p)
        letter2[x] = l
    for x in range (0, k):
        p = letterkey[x]
        l = associations.find(p)
        key2[x] = l
    cryptolist(letter2, key2)

       
       
       
    

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
    
        