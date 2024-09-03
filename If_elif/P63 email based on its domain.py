# Classify an email based on its domain:
# If the domain is @gmail.com, print Gmail,
# if it is @yahoo.com, print Yahoo, if it is @outlook.com,
# print Outlook. Otherwise, print Other.
# Example: Enter email address => example@yahoo.com
# Output: Yahoo

mail = input("Enter Gmail =")

if mail == '@gmail.com':
    print("Gmail Domain")
elif mail == '@yahoo.com':
    print("Yahoo Domain")
elif mail == '@outlook.com':
    print("Outlook Domain")
else:
    print("Wrong Domain")
