# 5.Replace Vowels with 8
f1=open("abc",'r')
while True:
    c=f1.read(1)
    if not c:
        break
    if c == 'a' or c == 'e' or c =='i' or c =='o' or c =='u':
        print(8,end="")
    else:
        print(c,end="")
print("\nEnd of file")
f1.close()
