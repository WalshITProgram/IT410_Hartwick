area_code = input("Please enter your area code: ")

if area_code:
    try:
        int(area_code)
        if len(area_code) == 3:
            print("Your area code is: " + area_code)
        else:
            print("Your inputted area code isnt long enough")
    except:
        print("You did provide a valid area code")
else:
    print("You did not enter an area code")