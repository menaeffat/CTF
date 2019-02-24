import os
from hashlib import sha256

def H(v):
    return int(sha256(str(v)).hexdigest(), 16)

def STEP(v):
    return (31338 * v**3 + 17 * v**2 + 2017 * v + 10) % 2**256

def encrypt(pt, key):
    state = H(key)
    ct = ""
    for c in pt:
        c = ord(c)
        for i in xrange(32):
            op = state % 4
            state = STEP(state)

            v = state % 256
            state = STEP(state)

            if op == 0:
                c = (c + v) % 256
            elif op == 1:
                c = (c ^ v) % 256
            elif op == 2:
                c = (c - v) % 256
            elif op == 3:
                c = (c * (v | 1)) % 256
        state ^= c
        ct += chr(c)
    return ct

def encrypt(pt):
    state = 47#H(key)
    ct = ""
    for c in pt:
        c = ord(c)
        for i in xrange(32):
            op = state % 4
            state = STEP(state)

            v = state % 256
            state = STEP(state)

            if op == 0:
                c = (c + v) % 256
            elif op == 1:
                c = (c ^ v) % 256
            elif op == 2:
                c = (c - v) % 256
            elif op == 3:
                c = (c * (v | 1)) % 256
        state ^= c
        ct += chr(c)
    return ct


ct = "868c017b7bef15e04ccc5f2d6b4c372fdff881080155".decode('hex')
pt = 'FLAG{'
while len(pt) < len(ct):
    c = chr(32)
    while encrypt(pt + c) != ct[:len(pt) + 1]: ## here you have to run the check for 
        ## for whole string (and not just single character) due to collision issue
        c = chr(ord(c) + 1)
    pt += c
print(pt)

##x = H(os.urandom(32))
##y = x % 256
##r = []
##for i in range(100):
##    xx = STEP(x) % 256
##    yy = STEP(y) % 256
##    if xx != yy :
##        print "wrong direction"
##    x = xx
##    y = yy
##    r.append(xx)
##print "suspicion verified"
##print r
