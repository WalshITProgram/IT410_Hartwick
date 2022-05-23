#declare empty employee data list
employeeData = []
#set increment count variable to 0
count = 0
while count < 5:
    # control variable for the employee check loop
    employeeIdCheck2 = False
    while employeeIdCheck2 == False:
        try: 
            # get employee id from user 
            employeeId = input("Please enter a employee id: ")
            # check employee id to see if it is a digit or greater than 7 digits
            employeeIdCheck = employeeId.isdigit()
            if len(employeeId) >= 8 or employeeIdCheck == False:
                employeeIdCheck2 == False
            else:
                break
        except:
            print("Employee id was not formatted correctly. Please try again. ")
    
    # employee name control variable
    employeeNameCheck2 = False
    while employeeNameCheck2 == False:
        try:
            # get employee name from user 
            employeeName = input("Please enter a first name: ")

            # check employee name for anything other than letters 
            employeeNameCheck = employeeName.isalpha()
            
            # declare bad characters list for name
            nameBadChars = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}',')']        

            # for loop to test if any unwanted characters are in the employees name
            hasBadCharacters = False
            for character in nameBadChars:
                if character in employeeName:
                    hasBadCharacters = True
            #test to see if bad characters came up in the for loop for address. If so we reprompt the user, otherwise it breaks the loop
            # The loop would also break if there are anything else other than numbers in the name because if employeeNameCheck comes back as false we would reprompt the user
            if hasBadCharacters == True or employeeNameCheck == False:
                employeeNameCheck2 = False
            else:
                break 
        except:
            print("Employee name was not properly formatted. Please try again. ")

    # declare email address control variable     
    emailAddressCheck2 = False
    # declare email address bad character list
    emailBadChars = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}',')']
    while emailAddressCheck2 == False:
        try:
            # get employee email address from user 
            employeeEmailAddress = input("Please enter an email address: ")

            # for loop to check unwanted characters in email bad chars
            for character in emailBadChars:
                if character in employeeEmailAddress:
                    hasBadCharacters = True
            
            # if there are bad characters in the email or anything other than letters we would reprompt the user. Otherwise we break the email address loop  
            if (hasBadCharacters == True) or (len(employeeEmailAddress) == 0):
                emailAddressCheck2 = False
            else:
                break
        except:
            print("Employee email was not properly formatted. Please try again. ")
    # declare home address control variable 
    employeeAddressCheck2 = False
    while employeeAddressCheck2 == False: 
        try: 
            # get employees home address from user 
            employeeAddress = input("Please enter the employee's home address(optional): ")
            # declare address bad characters list 
            addressBadChars = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>',  '?', ';', ':', '[', ']', '{', '}', ')']
            
            # for loop to check for bad characters in the address
            for charactor in addressBadChars:
                if character in employeeAddress:
                    hasBadCharacters = True
                    break
            # test to see if bad characters came up in the for loop for address. If so we reprompt the user, otherwise we break the loop
            if hasBadCharacters == True:
                employeeAddresscheck2 = False
            else:
                break
        except:
            print("Address was not properly formatted. Please try again. ")
    # append employee data into the dictionary
    # if an employee address is not provided or invalid the first if statement will be executed If an address is provided the else statement will be executed
    if len(employeeAddress) == 0: 
        employeeData.append({"EmployeeId": employeeId,"Name": employeeName.title(),"EmailAddress": employeeEmailAddress})
    else: 
        employeeData.append({"EmployeeId": employeeId,"Name": employeeName.title(),"EmailAddress": employeeEmailAddress,"HomeAddress": employeeAddress})
    
    # prompt the user if they want to enter another employee
    # if they type N we break the loop and print the dictionairy
    # if they type Y it would prompt them for another users input 
    enterAnotherEmployee = input("Would you like to enter data for another employee (type Y or N) ").lower()
    if enterAnotherEmployee == "n":
        break
    elif enterAnotherEmployee == "y":
        count += 1
        continue
    elif count >= 4:
        print("You can only enter data for 5 employees at a time. Goodbye!")
# print out the employee data dictionary
print("Here are the employee(s) that were entered into our database: ")
print(employeeData)