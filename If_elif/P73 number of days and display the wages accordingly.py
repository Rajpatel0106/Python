age = int(input("Enter Age ="))
gen = input("Enter Gender(M,F) =")

if 18 <= age < 30 and gen == 'M':
    print("700 Wage/day")
elif 18 <= age < 30 and gen == 'F':
    print("750 Wage/day")
elif 30 <= age <= 40 and gen == 'M':
    print("800 Wage/day")
elif 30 <= age <= 40 and gen == 'F':
    print("850 Wage/day")
else:
    print("wrong")
