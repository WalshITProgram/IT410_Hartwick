#declare program running variable
# this variable will become false it the user enters incorrect information  
programRunning = True
while programRunning:
    # get employee id from user 
    employeeId = input("Please enter your employee id: ")
    # check employee id to see if it is a digit or less then 7 digits
    employeeIdCheck = employeeId.isdigit()
    if len(employeeId) > 7 or employeeIdCheck == False:
        programRunning = False
        break

    # get employee name from user 
    employeeName = input("Please enter your first name: ")

    # check employee name for anything other than letters 
    employeeNameCheck = employeeName.isalpha()
    if employeeNameCheck == False:
        programRunning = False
        break

    # declare bad characters list for name
    nameBadChars = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}',')']        

    # for loop to test if any unwanted characters are in the employees name
    for character in nameBadChars:
        if character in employeeName:
            programRunning = False
            break
        
    # get employee email address from user 
    employeeEmailAddress = input("Please enter your email address: ")
    emailBadChars = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}',')']

    # test employees email address to see if any unneeded characters are in there
    if len(employeeEmailAddress) == 0:
        programRunning = False
        break
    
    for character in emailBadChars:
        if character in employeeEmailAddress:
            programRunning = False
            break


    
    # get employees home address from user 
    employeeAddress = input("Please enter your home address: ")

    # check employee address against the isalnum method to see if it has any unneeded characters
    employeeAddressCheck = employeeAddress.isalnum()
    addressBadChars = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>',  '?', ';', ':', '[', ']', '{', '}', ')']
    if employeeAddressCheck == False:
        programRunning = False
    for charactor in addressBadChars:
        if character in employeeAddress:
            programRunning = False
            employeeAddressCheck = False
            break
    # print out employee information
    # if the user didnt enter a address the first statement is executed 
    if len(employeeAddress) == 0 or employeeAddressCheck == False:
        print(f"Hello, {employeeName}. Your Employee ID is {employeeId}, and your email address is {employeeEmailAddress}. You did not provide a home address or it was invalid. ")
    else:
        print(f"Hello, {employeeName}. Your Employee ID is {employeeId}, and your email address is {employeeEmailAddress}. Your address is {employeeAddress}. ")
        
    
    # set the program running variable to false so the program doesnt run again
    programRunning = False

