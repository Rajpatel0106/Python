#2. Copy vowels in file v and consonants in file c.
f1 = open("abc",'r')
f2 = open("pqr",'w')
while True:
    c = f1.read(1)
    if not c:
        break
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        f2.write(c)