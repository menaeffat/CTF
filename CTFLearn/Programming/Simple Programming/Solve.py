f = open('data.dat','r')

x = f.read()

r = 0
for l in x.split('\n'):
    if l.count('0') % 3 == 0 or l.count('1') % 2 == 0:
        r += 1
print 'result is ', r-1
