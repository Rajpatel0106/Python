# Write a program to calculate Gross Salary and Net Salary print Grade of employee
Salary = float(input("Enter Salary ="))

Da = 0.52 * Salary
Ma = 0.10 * Salary
Hra = 0.10 * Salary
Va = 0.10 * Salary
itc = 0.5 * Salary
pf = Salary - 1000
Net_salary = Da + Ma + Hra + Va + itc + pf

print("Da =", Da)
print("Ma =", Ma)
print("Hra =", Hra)
print("Va =", Va)
print("itc =", itc)
print("Pf =", pf)

print("Gross salary =", Net_salary)
