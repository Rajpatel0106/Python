# 17. Let's say your expenses for every month are listed below:
#
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# June - 1980
# July - 2400
# August - 2250
# September - 2100
# October - 2400
# November - 2150
# December - 2500
#
# Create a Dictionary to store these monthly expenses and using that find out:

month ={"January":2200,"February":2350,"March":2600,"April":2130,"May":2190,"June":1980,
      "July":2400,"August":2250,"September":2100,"October":2400,"November":2150,"December":2500}

# 1.In February, how many dollars did you spend extra compared to January?
diff = month["January"] - month["February"]
print("spend extra compared to January =",-diff)

# 2.Calculate your total expenses for the first quarter (January to March) of the year.
total = month["January"] + month["February"] + month["March"]
print("Total Expenses of January to March =",total)

# 3.Check if you spent exactly 2400 dollars in any month.
for key,value in month.items():
    if value == 2400:
        print(key)

# 4.Modify the expense for June (2080 dollars) to your monthly expenses.
month["June"]= 2080
print(month)

# 5.You returned an item that you bought in April and received a refund of 200 dollars.
refund = month["April"] - 200
print(refund)

# 6.Determine which month had the highest expense and print the month and the amount.
value = month.values()
key = month.keys()
month = max(value)
print(month)

# 7.Calculate the average monthly expense for the first half of the year (January to June).
month ={"January":2200,"February":2350,"March":2600,"April":2130,"May":2190,"June":1980,
      "July":2400,"August":2250,"September":2100,"October":2400,"November":2150,"December":2500}

avg = month["January"] + month["February"] +month["March"] +month["April"] +month["May"] +month["June"]
print(avg / 6)

# 8.Find the month with the lowest expense and print the month and the amount.
value = month.values()
print(min(value))
