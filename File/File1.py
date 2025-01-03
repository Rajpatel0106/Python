# Print File Data as Column wise "⬇".
f1=open("abc",'r')

while True:
    c=f1.read(1)
    if not c:
        print("End of file")
        break
    print(c)
f1.close()