while True:
    # get employee id from user 
    employeeId = input("Please enter your employee id: ")
    # check employee id to see if it is a digit or greater than 7 digits
    employeeIdCheck = employeeId.isdigit()
    if len(employeeId) > 7 or employeeIdCheck == False:
        break

    # get employee name from user 
    employeeName = input("Please enter your first name: ")

    # check employee name for anything other than letters 
    employeeNameCheck = employeeName.isalpha()
    
    # declare bad characters list for name
    nameBadChars = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}',')']        

    # for loop to test if any unwanted characters are in the employees name
    hasBadCharacters = False
    for character in nameBadChars:
        if character in employeeName:
            hasBadCharacters = True

    # check the has bas characters variable to see if it is less than 
    if hasBadCharacters == True or employeeNameCheck == False:
        break
        
    # get employee email address from user 
    employeeEmailAddress = input("Please enter your email address: ")

    # declare email bad characters
    emailBadChars = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}',')']
    
    employeeEmailAddressCheck = employeeEmailAddress.isalnum()
    # check to see if the email is left blank 
    if len(employeeEmailAddress) == 0:
        break
    # for loop to check unwanted characters in email bad chars
    for character in emailBadChars:
        if character in employeeEmailAddress:
            hasBadCharacters = True
    
    # if there are bad characters in the email or anything other than letters we would break 
    if hasBadCharacters == True or employeeEmailAddressCheck == False:
        break

    
    # get employees home address from user 
    employeeAddress = input("Please enter the employee's home address(optional): ")
    # declare address bad characters list 
    addressBadChars = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>',  '?', ';', ':', '[', ']', '{', '}', ')']
    
    # for loop to loop the different characters in address bad chars
    for charactor in addressBadChars:
        if character in employeeAddress:
            hasBadCharacters = True
            break
    if hasBadCharacters == True:
        break
    # print out employee information
    # if the user didnt enter a address the first if statement is executed. If the employee address was valid, the else statement is exdcuted
    if len(employeeAddress) == 0:
        print(f"Hello, {employeeName}. Your Employee ID is {employeeId}, and your email address is {employeeEmailAddress}. You did not provide a home address ")
    else:
        print(f"Hello, {employeeName.title()}. Your Employee ID is {employeeId}, and your email address is {employeeEmailAddress}. Your address is {employeeAddress}. ")
    
    # final break statement so the loop doesnt execute again
    break
    

