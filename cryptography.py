"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""


    
def assoc(listreal, d):
    r = False
    listnuml = len(listreal)
    listlet = listreal[:]
    for g in range (0, listnuml):
        x = listreal[g]
        if x > 84:
            w = x - 85
            listlet[g] = associations[w]
        if x < 84:
            listlet[g] = associations[x]
    return listlet
            
def cryptolist(letter2, key2, d):
    r = len(letter2)
    k = len(key2)
    if r > k:
        range1 = r
        listreal = letter2[:]
    if r < k:
        range1 = k
        listreal = key2[:]
    if r == k:
        range1 = k
        listreal = key2[:]
    rp = False
    np = False
    z = 0
    j = 0
    for x in range(0, range1):
        if x >= r:
            z = x%r
            np = True
        if x >= k:
            z = x%k
            rp = True
        if rp == True:
            valuem = letter2[x]
            valuen = key2[z]
            j = 1
        if np == True:
            valuem = letter2[z]
            valuen = key2[x]
            j = 1
        if j == 0:
            valuem = letter2[x]
            valuen = key2[x]
        if d == False:
            valueg = valuem + valuen
            listreal[x] = valueg
        if d == True:
            valueg = valuem - valuen
            listreal[x] = valueg
    return listreal
    

def efunction (i, m, k, d):
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
    listreal = cryptolist(letter2, key2, d)
    listlet = assoc(listreal, d)
    return listlet

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
x = 0
while x == 0:
    i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if i == "e" or i == "d":
        m = input("Message: ")
        k = input("Key: ")
        d = False
        if i == "e":
            listlet = efunction (i, m, k, d)
            stre = ''.join(listlet)
            print(stre)
            print (" ")
        if i == "d":
            d = True
            listlet = efunction (i, m, k, d)
            stre = ''.join(listlet)
            print(stre)
            print(" ")
    elif i == "q":
        print ("Goodbye!")
        x = 1
    else:
        print ("Did not understand command, try again.")
        print (" ")
    
        