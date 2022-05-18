program_running = True

while program_running:
    area_code = input("Please enter your area code: ")
    area_code_ok = False
    
    while not area_code_ok:
        if area_code:
            try:
                int(area_code)
                if len(area_code) == 3:
                    print("Your area code is: " + area_code)
                    area_code_ok = True
                else:
                   area_code_ok = False
            except:
                area_code_ok = False
        else:
            area_code_ok = False
        
        if not area_code_ok:
            area_code = input("Area code was not properly formatted. Please try again: ")
    add_another_number = input("Do you wish to enter another phone number? (Y or N) ")
    if add_another_number == "N":
        break
    else:
        continue