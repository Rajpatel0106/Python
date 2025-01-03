#3. Merge two files in the third file
f1 = open("abc",'r')
f2 = open("pqr",'r')
f3 = open("qwe",'w')
while True:
    c = f1.read(1)
    if not c:
        break
    f3.write(c)
while True:
    c1 = f2.read(1)
    if not c1:
        break
    f3.write(c1)
f1.close()
f2.close()
f3.close()

#upper in different and lower in different
f1=open("abc" , "r")
f2=open("pqr","w")
f3=open("qwe","w")
while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch.isupper():
        f2.write(ch)
    else:
        f3.write(ch)
f1.close()
f2.close()
f3.close()
print("Copied")