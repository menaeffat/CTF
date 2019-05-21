l = '\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'

x = map(ord,list(l))


p = 'ctflearn{'
p = map(ord,list(p))


r = []

for i in range(len(p)):
    r.append(p[i] ^ x[i])

k = [106, 111, 119, 108, 115]

r = []

for i in range(len(x)):
    r.append(k[i%len(k)] ^ x[i])

print ''.join(map(chr,r))
