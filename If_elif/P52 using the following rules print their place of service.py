age = int(input("Enter Your age ="))
gen = input("Enter Your Gender (Male or Female) =")
ms = input("Enter Your Marital status (Yes or No) =")

if gen == 'Female':
    print("You work only in urban areas")
elif gen == 'Male' and 20 <= age <= 40:
    print("You may work in anywhere")
elif gen == 'Male' and 40 < age <= 60:
    print("You work in urban areas only")
else:
    print("Error")
