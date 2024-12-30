# 18. You and your wife argued about expenses last night. You both want to know who is spending more in a month. Now you both go to the Little Yoda he is a good python programmer. He suggested that both of you add an entry in a dictionary next time you spend money. So that you can have a clear picture of your expenses and plan to reduce them. Both dictionaries are as below-
# Your expenses -
#
# Clothes - 1100
# Shoes - 1000
# Watch - 900
# Mobile Recharge - 699
# Petrol - 1980
# Your Wife’s expenses -
#
# Mobile Recharge - 799
# DTH recharge - 999
# Clothes - 2310
# Makeup - 3670
# Shoes - 999


Your_expenses ={"Clothes" :1100,"Shoes":1000,"Watch" : 900,"Mobile Recharge": 699,"Petrol":1980,}
wife_expenses ={"Mobile Recharge": 799,"DTH recharge" : 999,"Clothes" : 2310,"Makeup" : 3670,"Shoes" : 999}

# Find out the total expenses for each of you.
values = Your_expenses.values()
values1 =wife_expenses.values()
sum1 = sum(values) + sum(values1)
print("Your Expenses =",sum(values),"\nWife Expenses =",sum(values1))

# Find out who spending more
values = Your_expenses.values()
values1 =wife_expenses.values()
if sum(values) > sum(values1):
    print("You Spend more")
else:
    print("Wife Spend more")

# Find out which thing you and your wife spending more
values = Your_expenses.values()
values1 =wife_expenses.values()
print("Your Expense thing = ",max(values),"\nWife Expense thing =",max(values1))