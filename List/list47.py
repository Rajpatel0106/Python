# 1.Write a program that asks user to enter a city name and it should tell which country the city belongs to
city = input("Enter your city name =")

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

if city in india:
    print("India")
elif city in pakistan:
    print("Pakistan")
elif city in bangladesh:
    print("Bangladesh")
else:
    print("sorry")

# 2.Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka
# it should print "They don't belong to same country"
city1 = input("Enter First city name =")
city2 = input("Enter Second city name =")

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")
