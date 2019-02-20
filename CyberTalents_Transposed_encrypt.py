#-*- coding:utf-8 -*-

def revs(s):
    s = s[1:] + s[:1]
    s = s[0::2] + s[1::2]
    s = s[1:] + s[:1]
    return s

def fors(s, w, perm):
    r = ""
    for j in xrange(0, len(s), w):
        for k in xrange(w):
            r += s[j:j+w][perm[k]]
    s = r
    return s

def revso(s):
    s = s[-1:] + s[:-1]
    l = int(round(len(s)/2.0))
    r = ''
    for i in range(l):
        r += s[i] + (s[l+i] if l+i<len(s) else '')
    s = r
    s = s[-1:] + s[:-1]
    return s

c = 'L{NTP#AGLCSF.#OAR4A#STOL11__}PYCCTO1N#RS.S'
W = 7
import itertools

for i in itertools.permutations(range(W),W):
    x = c
    for a in xrange(100):
        x = fors(x,W,list(i))
        x = revso(x)
    if 'FLAG{' in x:
        print x, i
        break

##x = revs('012345678000')
##print x
##y = revso(x)
##print y

##import random


##perm = range(W)
##random.shuffle(perm)

#msg = open("flag.txt").read().strip()
##msg = 'FLAG{0000000000000000000000000000000000}'
##msg = '0987654321098765432109876543210987654321'
##x  = len(msg)
##while len(msg) % (2*W):
##    msg += "."
##
###print "1:", x, len(msg), msg
##
##for i in xrange(100):
##    msg = revs(msg)
##    msg = fors(msg,W,perm)
##print msg

##
##cypher = 'L{NTP#AGLCSF.#OAR4A#STOL11__}PYCCTO1N#RS.S'
##msg =    'FLAG{0000000000000000000000000000000000}'

