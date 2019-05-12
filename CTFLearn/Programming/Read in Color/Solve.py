from PIL import Image

i = Image.open('color_img.png')

s = []
for d in range(0,i.size[0],50):
    x = i.getpixel((d,0))
    s.append(x)

r = list((s))

y = [''.join([chr(i) for i in x]) for x in r]
print ''.join(y)
