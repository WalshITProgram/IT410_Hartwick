employeeData = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

# declare empty lists that we will add data into later
employeeNumbers = []
employeeNames = []
employeeSalary = []

# for loop to sort the data into their respective lists
for data in employeeData:
    if data not in employeeNumbers and type(data) == int:
        employeeNumbers.append(data)
    elif data not in employeeNames and type(data) == str:
        employeeNames.append(data)
    elif data not in employeeSalary and type(data) == float:
        employeeSalary.append(data)
# declare total hourly rate list
total_hourly_rate = []
# loop to multiply employee salary by 1.3 
for count in range(0,len(employeeSalary)):
    newSalary = employeeSalary[count] * 1.3
    total_hourly_rate.append(newSalary)
maxValue = 0

# for loop to determine the max total hourly rate value
for count in range(0,len(total_hourly_rate)):
    if total_hourly_rate[count] > maxValue:
        maxValue = total_hourly_rate[count]

# edit this later joe! and delete this comment 
if maxValue > 37.30:
    print(maxValue, "'s employee salary could be a budget concern")

# declare underpaid salaries list
underpaid_salaries = []
# for loop to fill the underpaid salaries list
for count in range(0,len(total_hourly_rate)):
    if (total_hourly_rate[count] > 28.15) and (total_hourly_rate[count] < 30.65):
        underpaid_salaries.append(total_hourly_rate[count])
companyRaises = []

for count in range(0,len(total_hourly_rate)):
    if total_hourly_rate[count] >= 22 and total_hourly_rate[count] <= 24:
        companyRaises.append(total_hourly_rate[count])
print(companyRaises)





