from PIL import Image

i = Image.open('out copy.jpg')
d = 304
for w in [d,i.size[0]/d]:
    n = Image.new("RGB",(w,i.size[0]/w+1))

    for x in range(i.size[0]):
        n.putpixel((x%w,x/w),i.getpixel((x,0)))

    n.save('out {:02}.jpg'.format(w))
print "done"
