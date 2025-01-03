# Copy your data to another data file like
f1=open("abc",'r') #abc is f1 file
f2=open("pqr",'w')#pqr is f2 file
while True:
    c=f1.read(1)
    if not c:
        break
    f2.write(c)#f1 to copy data in f2
f1.close()
f2.close()
print("Copied")