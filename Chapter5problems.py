# problem 5-1
# this condition would evaulate to false
number = 5
print(number == 4)
# this condition would evaulate to true
speed = 75.5
print(speed == 75.5)
# this condition will evaulate to false
favCoaster = "Dragster"
print(favCoaster == "Millenium Force")
# this condition will evaulate to true
addition = 2 + 2
print(addition == 4)
# this condition will evaulate to false 
strLessThan = "orange"
print(strLessThan < "apple")
# this condition will evaulate to true
multiplication = 3 * 3
print(multiplication < 10)

#problem 5-2
# declare variables 
sixNum = 6
threeNum = 3
# if statement test to determine if the numbers are odd
if sixNum % 2 == 1:
    print("Number 6 is odd")
if threeNum % 2 == 1:
    print("Number 3 is odd")

# problem 5-3
# modifed if statement test on sixNum 
if sixNum % 2 == 1:
    print("Number 6 is odd")
else:
    sixNum = sixNum + 1
    print(sixNum, " is odd")

# problem 5-4
# declare list
favFruits = ["Banana", "Apple", "Orange"]

# check length of list 
if len(favFruits) == 2:
    print("I like 2 fruits")
elif len(favFruits) == 3:
    print("I like 3 fruits")
elif len(favFruits) == 4:
    print("I like 4 fruits")
else:
    print("I like several fruits")

#problem 5-5
# declare list
numberList = list(range(1,56))
# declare number variables
number1 = 25
number2 = 17
# loop through the list to find number 25
for number in numberList:
    if number == number1:
        print("Number 25 is found!")
    else: 
        print("Number 25 is not found")
# loop through the list to find number 17
for number in numberList:
    if number == number2:
        print("Number 17 is found")
    else:
        print("Number 17 is not found")

# problem 5-6
# declare both fav stores list and store sales list
favStores = ["Target", "Best Buy", "Amazon", "Gardner White"]
storeSales = ["Target", "Gardner White"]
# check to see if the stores are currenly running a sale 
for store in favStores:
    if store in storeSales:
        print(store, "is currenly running a sale!")
    else:
        print(store, "is not currenly running a sale!")

