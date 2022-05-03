# declare walsh course list step 1
courseList = ["it 402", "qm 202", "com 320", "com 340", "it 410", "it 405"]

# sort course list and loop through each course step 2
courseList.sort()

for course in range(0,len(courseList)):
    print("I have taken " + courseList[course].upper() + " at Walsh College")

# add courses that I plan to take next term to the list step 3 part 1
courseList.append("it 412")
courseList.append("it 407")
courseList.sort()

# loop through the list step 3 part 2
print("\nThis is my course of study with upcoming courses added:\n")
for course in range(0,len(courseList)):
    print("I have taken " + courseList[course].upper() + " at Walsh College")

# remove course I have already taken step 4
print("\nI do not have to take these courses:")
print(courseList[0].upper(), courseList[1].upper(), courseList[2].upper())
print(courseList[3].upper(),courseList[5].upper(), courseList[7].upper())
del courseList[0:2]
del courseList[0]
del courseList[0]
del courseList[1]
del courseList[2]

# print courses that I will take next term step 5 
print("\nI plan to take the following courses next term")
for course in range(0,len(courseList)):
    print(courseList[course].upper())

#create list of numbers that are divisble by 6  step 6
divisibleBySix =[]
for number in range (6,1001,6):
    divisibleBySix.append(number)

#display first 20 numbers in the divisible by 6 list step 7
print("\nHere are twenty numbers divisible by 6:")
for count in range(0,20):
    print(divisibleBySix[count])

# calculate max value step 8
maxValue = max(divisibleBySix)

# print max value  of the divisible by 6 list step 9
print("\nThe maximum value in the list is:", maxValue)

# calculate and print sum between the 10th and 50th item step 10
total = 0
for number in range(10,51):
    total = total + divisibleBySix[number]

print("\nHere is the sum of several values in the list:", total)

#overwrite walsh course list with the divisble by 6 list step 11
courseList = divisibleBySix
