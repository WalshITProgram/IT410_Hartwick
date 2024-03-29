# declare the person class
class Person():
    """This class will be extended into the student and instructor classes"""
    def __init__(self, name, emailAddress, personID):
        """Intializes the attrbiute of the person class"""
        self.name = name
        self.emailAddress = emailAddress
        self.personID = personID
# declare the student class that will store each students record 
class Student(Person):
    """This class stores the student records"""
    def __init__(self, name, emailAddress, studentID, programStudy):
        """This constructor intializes the student attributes"""
        super().__init__(name, emailAddress, studentID)
        self.programStudy = programStudy
    def displayInformation(self):
        """This method displays the students attributes"""
        print(f"{self.name.title()}'s id number is {self.personID}, his program of study is {self.programStudy}, and his email address is {self.emailAddress}")
# declare the instructor class that will store information about the instructor
class Instructor(Person):
    """This class stores the instructor records"""
    def __init__(self, name, emailAddress, instructorID, institution, highestDegree):
        """This constructor intializes the instructor attributes"""
        super().__init__(name, emailAddress, instructorID)
        self.institution = institution
        self.highestDegree = highestDegree
    def displayInformation(self):
        """This method displays the instructors attributes"""
        print(f"{self.name.title()}'s id number is {self.instructorID} and his email address is {self.emailAddress}.")
        print(f"The highest degree {self.name.title()} earned is {self.highestDegree} and the recent college attended was {self.institution}")
# declare the Validator class that will use different methods to validate submitted information 
class Validator():
    def __init__(self):
        """This constructor is empty because there are no real attrbiutes this class has"""
    
    def validateEmail(self, email):
        """This method validates the email inputted by the user"""
        badCharacters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", '"\"', ")"]
        hasBadCharacters = False
        # for loop to determine if there are any bad characters in the name
        for character in badCharacters:
            if character in email:
                hasBadCharacters = True
                break
        # if the hasBadCharacters variable comes back as true we will return false, otherwise it will return true
        if hasBadCharacters == True or len(email) == 0:
            return False
        else:
            return True
    def validatePersonID(self, personID, maxLength):
        """This method validates the instructorID inputted by the user"""
        # if the instructorID has anything other than digits in it or if it is more than 5 digits we would return false. Otherwise it will return true
        digitTest = personID.isdigit()
        if digitTest == False or len(personID) > maxLength:
            return False
        else:
            return True

    def validateName(self, name):
        """This method validates the name inputed by the user"""
        badCharacters = ["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}"]
        hasBadCharacters = False
        # for loop to determine if there are any bad characters in the name
        for character in badCharacters:
            if character in name:
                hasBadCharacters = True
                break
        # if the hasBadCharacters variable comes back as true we will return false, otherwise it will return true
        if hasBadCharacters == True or len(name) == 0:
            return False
        else:
            return True
    
    
    


# declare empty college records list that will be filled later 
college_records = []
# declare outer while loop control variable 
anotherUser = "yes"

# start outer while loop: if the user enters q after entering in a record, then the program will exit
while anotherUser != "q":
    # start individalType while loop that will continue until the user enter S for student or I for instuctor
    while True:
        individualType = input("What type of individual are you entering data for? Enter S for student or I for instructor: ").lower()
        # if the user enters s or i then the loop will break and move onto the next item. Otherwise, it will give them a formatting error and tell the user to try again
        if individualType == "s" or  individualType == "i":
            break
        else:
            print("Type of individual was not properly formatted. Please try again. ")
    # declare a person object of validator that will be used to validate different inputs
    person = Validator()
    # start name while loop that will continue until the user enters a valid name
    while True:
        name = input("Please enter a name: ")
        # calling my validate name method. If it comes back as false, we will prompt the user to enter the name again. Otherwise the name loop will break 
        validName = person.validateName(name)
        if validName == False:
            print("Name was not properly formatted. Please try again.")
        else:
            break
    # start email address while loop that will continue until the user enters a valid email address
    while True:
        emailAddress = input("Please enter a email address: ")
        validEmail = person.validateEmail(emailAddress)
        # calling my validate email addres method. If it comes back as false, we will prompt the user to enter the email address again. Otherwise the email address loop will break
        if validEmail == False:
            print("Email address was not properly formatted. Please try again. ")
        else:
            break
    # if the user entered s for student then we will prompt them for their id and program oof study. 
    if individualType == "s":
        # start student id while loop that will continue until the user enters a valid student id
        while True:
            studentId = input("Please enter your student id: ")
             # calling my validate student id method. If it comes back as false, we will prompt the user to enter the student id again. Otherwise the student id loop will break
            validStudentID = person.validatePersonID(studentId, 7)
            if validStudentID == False:
                print("Student id was not properly formatted. Please try again")
            else:
                break
        # start program of study while loop that will continue until the user enters a valid program of study 
        while True:
            programStudy = input("Please enter your program of study: ")
            # if the user left the program of study feild blank then we will prompt them to enter it again. Otherwise, thw program of study loop will break. 
            if len(programStudy) == 0:
                print("The program of study field is required. Please try again.")
            else:
                break
        # after all the information is collected I would create a student object
        # I will also append the entry to my college records list and then call my student displayInformation method that will display the student's information
        student = Student(name, emailAddress, studentId, programStudy)
        college_records.append(student)
        college_records.append(student.emailAddress)
        college_records.append(student.personID)
        college_records.append(student.programStudy)
        student.displayInformation()
    # if the user didnt enter s, then I Assume that the user entered I for instructor. 
    # In that case, we would prompt them for their instructorID, last college attended and highest degree earned 
    else:
         # start instructor ID while loop that will continue until the user enters a valid instructor ID
        while True:
            instructorId = input("Please enter your instructor ID: ")
            # calling my validate instructor id method. If it comes back as false, we will prompt the user to enter the instructor id again. Otherwise the instructor id loop will break
            validInstructorID =  person.validatePersonID(instructorId, 5)
            if validInstructorID == False:
                print("Instructor id was not properly formatted. Please try again")
            else:
                break
         # start last college attended while loop that will continue until the user enters a valid college they attended 
        while True: 
            college = input("Please enter the last institution you attended: ")
            # if the user left the last college attended field blank then we will prompt them to enter it again. Otherwise, the college loop will break
            if len(college) == 0:
                print("The last college attended field is required. Please try again.")
            else:
                break
        # start degree earned while loop that will continue until the user enters a valid degree
        while True:
            degreeEarned = input("Please entert your highest degree earned: ")
            # if the user left the degree earned field blank then we will prompt them to enter it again. Otherwise, the degree earned loop will break
            if len(degreeEarned) == 0:
                print("The last degree earned field is required. Please try again.")
            else:
                break
        # after all the information is collected I would create an instructor object
        # I will also append the entry to my college records list and then call my student displayInformation method that will display the student's information
        instructor = Instructor(name, emailAddress, instructorId, college, degreeEarned)
        college_records.append(instructor.name)
        college_records.append(instructor.emailAddress)
        college_records.append(instructor.instructorID)
        college_records.append(instructor.institution)
        college_records.append(instructor.highestDegree)

        instructor.displayInformation()
    # if the user enters Q the loop will break. Otherwise, if the user enters any other character it will continue
    anotherUser = input("Enter Q to quit or any other keyboard character to continue entering data: ").lower()
# display college_records list that will have all the data entered during this session
print("Here is the data entered into our database during this session: ")
for record in college_records:
    print(record)
        

