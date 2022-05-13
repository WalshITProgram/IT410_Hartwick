# declare employee data list step #1
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

# declare empty lists that I will add data into later step #2A
employeeNumbers = []
employeeNames = []
employeeSalary = []

# for loop to sort the data into their respective lists 
# step #2b and step 3
for data in employeeData:
    if data not in employeeNumbers and type(data) == int:
        employeeNumbers.append(data)
    elif data not in employeeNames and type(data) == str:
        employeeNames.append(data)
    elif data not in employeeSalary and type(data) == float:
        employeeSalary.append(data)
# declare total hourly rate list step 4A
total_hourly_rate = []

# loop to multiply the employee's salary by 1.3 step 4b 
for count in range(0,len(employeeSalary)):
    newSalary = employeeSalary[count] * 1.3
    total_hourly_rate.append(newSalary)
maxValue = 0

# for loop to determine the max total hourly rate value step 4c
for count in range(0,len(total_hourly_rate)):
    if total_hourly_rate[count] > maxValue:
        maxValue = total_hourly_rate[count]

# determine max value step 4d
if maxValue > 37.30:
    print(f"${maxValue} could be a budget concern regarding salary")

# declare underpaid salaries list step 5a
underpaid_salaries = []

# for loop to fill the underpaid salaries list step 5b 
for count in range(0,len(total_hourly_rate)):
    if total_hourly_rate[count] > 28.15 and total_hourly_rate[count] < 30.65:
        underpaid_salaries.append(total_hourly_rate[count])

# declare company raises list step 6a
companyRaises = []


# for loop to fill the company raises list step 6b
for count in range(0,len(employeeSalary)):
    if (employeeSalary[count] >= 22) and (employeeSalary[count] <= 24):
        newSalary = employeeSalary[count] * 1.05
        companyRaises.append(newSalary)
    elif (employeeSalary[count] >= 24) and (employeeSalary[count] <= 26):
        newSalary = employeeSalary[count] * 1.04
        companyRaises.append(newSalary)
    elif (employeeSalary[count] >= 26) and (employeeSalary[count] <= 28):
        newSalary = employeeSalary[count] * 1.03
        companyRaises.append(newSalary)
    else:
        newSalary = employeeSalary[count] * 1.02
        companyRaises.append(newSalary)



# finding the person with the highest salary in the list and findind his id number and information in the list.  
# Then since he has the highest salary, he is supervisor step 7
for count in range(0,len(employeeSalary)):
    if employeeSalary[count] >= 26 and employeeSalary[count] <= 29 and employeeNames[count] == "Dion Green" and employeeNumbers[count] == 1127:
        print(f"Our supervisors name is: {employeeNames[count]}.\nHis salary is ${employeeSalary[count]}.\nFinally, his employee id number is: {employeeNumbers[count]}")








