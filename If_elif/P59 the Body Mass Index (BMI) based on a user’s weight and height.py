wt = float(input("Enter Weight(kg) ="))
ht = float(input("Enter Height(M) ="))

bmi = wt / (ht * ht)
print("Your BMI =", bmi)

if bmi < 18.5:
    print("underweight")
elif 18.5 < bmi < 25:
    print("normal weight")
elif 25 < bmi < 30:
    print("slightly overweight")
elif 30 < bmi < 35:
    print("obese")
elif bmi > 35:
    print("clinically obese")
else:
    print("Wrong ")
