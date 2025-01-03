# 4.Print only Vowels
f1=open("abc",'r')
while True:
    c=f1.read(1)
    if not c:
        break
    if c == 'a' or c == 'e' or c =='i' or c =='o' or c =='u':
        print(c)
print("\nEnd of file")
f1.close()
