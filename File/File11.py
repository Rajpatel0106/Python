#1. Copy without spaces
f1 = open("abc",'r')
f2 = open("pqr",'w')
while True:
    c = f1.read(1)
    if not c:
        break
    if c == " ":
        print("",end="")
    else:
        f2.write(c)