# 15. We have the following information on countries and
# their population (population is in cores),
# Country Population
# China 	143
# India 	136
# USA 	32
# UK 	21
# Using above create a dictionary of countries and its population
# Write a program that asks user for 4 type of inputs,
# option 1 print: if user enter print
# then it should print all countries with their population in this format,
#         china==>143
#         india==>136
#         usa==>32
#         uk==>21
# option 2 add: if user input add then it should further ask for a country name to add.
# If country already exist in our dataset then it should print that
# it exist and do nothing. If it doesn't then it asks for population and
# add that new country/population in our dictionary and print it

# Option 3 remove: when user inputs remove it should ask for a country to remove.
# If country exists in our dictionary then remove it and print a new dictionary using the
#  format shown above in (a). Else print that country doesn't exist!

# option 4 query: on this again ask user for which country he or she wants to query.
# When user inputs that are country, it will print the population of that country.

# Country Population
# China	143
# India	136
# USA	32
# UK	21
#
Country={"China":143,"India":136,"Usa":32,"Uk":21}
print("Press 1 For All Data")
print("Press 2 For Add Data")
print("Press 3 For Remove Data")
print("Press 4 For Show Population")
op = int(input("Enter Option ="))
if op == 1:
    for key,value in Country.items():
        print(key,"==>",value)
elif op == 2:
    cou = input("Enter Country =")
    if cou in Country:
        print("That is Exist")
    else:
        po = int(input("Enter Population ="))
        Country[cou]=po
        print(Country)
elif op == 3:
    cou = input("Enter Country =")
    if cou in Country:
        Country.pop(cou)
        print(Country)
        cou = input("Enter Country =")
        po = int(input("Enter Population ="))
        Country[cou] = po
        print(Country)
    else:
        print("that country doesn't exist!")
elif op == 4:
    cou = input("Enter Country =")
    print("Country","Population")
    for key,value in Country.items():
        if cou in Country:
            print(key,value)
        else:
            print("Not Exist")
            break
else:
    print("Wrong Option")
