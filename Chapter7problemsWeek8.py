# problem 7-1
# get favorite restaurant from the user 
favRestaurant = input("Please enter your favorite restaurant: ")
# print their favorite restaurant out 
print("Let me help you find the closest " + favRestaurant)

# problem 7-2
# get 2 numbers from user 
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
# determine the product of both numbers
product = num1 * num2
# display the product
print(f"The product of both these numbers is {product}")

# problem 7-3
# declare empty lsit to fill later 
dinnerItems = []
#prompt the user for input
dinnerItem = input("Enter a item you plan on having for dinner or enter Q to quit  ")
# append the value to the list if the user's responce doesnt equal Q 
if dinnerItem != "Q":
    dinnerItems.append(dinnerItem)
# declare while loop to fill the users dinner plan 
while dinnerItem != "Q":
    dinnerItem = input("Enter a item you plan on having for dinner or enter Q to quit  ")
    if dinnerItem != "Q":
        dinnerItems.append(dinnerItem)
# print out the users dinner plans unless the user didnt enter any
if len(dinnerItems) != 0:
    print("Here are your dinner plans: ")
for item in dinnerItems:
    print(item)

# problem 7-4
# get input from the user
carnivalRide = input("Which carnival ride would you like to go on? Press F for ferris wheel, T for tilt-a-whirl, P for pirate ship or Q to quit ")
# determine which ride they want to go on 
if carnivalRide == "F":
    print("The ferris wheel costs $2.")
elif carnivalRide == "T":
    print("The tilt-a-whirl costs $3.")
elif carnivalRide == "P":
    print("The pirate ship costs $3.50.")
elif carnivalRide != "Q":
    print("This ride wasnt found. Please try again. ")
# while loop that continues until the user presses Q
while carnivalRide != "Q":
    carnivalRide = input("Which carnival ride would you like to go on? Press F for ferris wheel, T for tilt-a-whirl, P for pirate ship or Q to quit  ")
    if carnivalRide == "F":
        print("The ferris wheel costs $2.")
    elif carnivalRide == "T":
        print("The tilt-a-whirl costs $3.")
    elif carnivalRide == "P":
        print("The pirate ship costs $3.50.")
    elif carnivalRide != "Q":
        print("This ride wasnt found. Please try again. ")

# problem 7-5
# declare grocery list
groceryStoreList = ["Chef Boyardee Beefaroni", "Campbell's Soup", "Quaker's Oatmeal", "Pretzel Combos", "Chex mix", "Cheez Its", "Chef Boyardee Beefaroni"]

# loop through the instance of Chef boyardee Beefaroni and remove them 
count = 0
while count < len(groceryStoreList):
    if groceryStoreList[count] == "Chef Boyardee Beefaroni":
        groceryStoreList.remove(groceryStoreList[count])
    count += 1
# print out the remaining items
print(groceryStoreList)