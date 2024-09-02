# Ask the user for their salary and years of employment.
# Determine loan eligibility based on these criteria:
# salary above 50,000 and employment greater than 2 years =
# Eligible for loan, otherwise Not eligible for loan.
# (Example: Enter salary => 60000, Enter years of employment => 3)

No = int(input("Enter Amount ="))
year = int(input("Enter years of employment ="))

if No > 50000 and year > 2:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
