# declare employee data list 
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

# declare empty lists that I will add data into later 
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

# loop to multiply the employee's salary by 1.3 
for count in range(0,len(employeeSalary)):
    newSalary = employeeSalary[count] * 1.3
    total_hourly_rate.append(newSalary)
maxValue = 0

# for loop to determine the max total hourly rate value 
for count in range(0,len(total_hourly_rate)):
    if total_hourly_rate[count] > maxValue:
        maxValue = total_hourly_rate[count]

# determine max value 
if maxValue > 37.30:
    print(f"${maxValue} could be a budget concern regarding salary")

# declare underpaid salaries list 
underpaid_salaries = []

# for loop to fill the underpaid salaries list 
for count in range(0,len(total_hourly_rate)):
    if total_hourly_rate[count] > 28.15 and total_hourly_rate[count] < 30.65:
        underpaid_salaries.append(total_hourly_rate[count])

# declare company raises list 
companyRaises = []


# for loop to fill the company raises list 
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

# declare NEW dictionary list that will combine all of the employee lists
employeeDictionairy = [{"Employee Number" : employeeNumbers[0], "Employee Name" : employeeNames[0], "Employee Salary" : employeeSalary[0],"Total hourly rate:": total_hourly_rate[0], "Company Raises" : companyRaises[0]},
                    {"Employee Number" : employeeNumbers[1], "Employee Name" : employeeNames[1], "Employee Salary" : employeeSalary[1],"Total hourly rate:": total_hourly_rate[1], "Company Raises" : companyRaises[1]},
                     {"Employee Number" : employeeNumbers[2], "Employee Name" : employeeNames[2], "Employee Salary" : employeeSalary[2],"Total hourly rate:": total_hourly_rate[2], "Company Raises" : companyRaises[2]},
                     {"Employee Number" : employeeNumbers[3], "Employee Name" : employeeNames[3], "Employee Salary" : employeeSalary[3],"Total hourly rate:": total_hourly_rate[3], "Company Raises" : companyRaises[3]},
                     {"Employee Number" : employeeNumbers[4], "Employee Name" : employeeNames[4], "Employee Salary" : employeeSalary[4],"Total hourly rate:": total_hourly_rate[4], "Company Raises" : companyRaises[4]},
                     {"Employee Number" : employeeNumbers[5], "Employee Name" : employeeNames[5], "Employee Salary" : employeeSalary[5],"Total hourly rate:": total_hourly_rate[5], "Company Raises" : companyRaises[5]},
                     {"Employee Number" : employeeNumbers[6], "Employee Name" : employeeNames[6], "Employee Salary" : employeeSalary[6],"Total hourly rate:": total_hourly_rate[6], "Company Raises" : companyRaises[6]},
                     {"Employee Number" : employeeNumbers[7], "Employee Name" : employeeNames[7], "Employee Salary" : employeeSalary[7],"Total hourly rate:": total_hourly_rate[7], "Company Raises" : companyRaises[7]}]
#using a for loop to print out all of the dictinairy items  
print("Employee dictionairy list:")                  
for employee in employeeDictionairy:
    print(employee)









