# 4-1
favPlacesVisit = ["Sandusky", "Charlotte", "Gatlinburg", "Frankenmuth"]
for place in favPlacesVisit:
    print(place + " is a nice place to visit")
#4-2
for number in range(90,101):
    print(number)
#4-3
numbers = list(range(100000,1000000))
print(sum(numbers))

#4-4
ranNumbers = [5,1,67,87,7,8,90,800, 700, 600, 850, 840, 740, 630, 15, 17, 87, 0, 100, 99]
print(min(ranNumbers))
print(max(ranNumbers))

#4-5
muilpleFive = list(range(5,101, 5))
print(muilpleFive)

#4-6
twentyToThirty = list(range(20,31))
print(twentyToThirty)
twentyToThirty = [value * 2 for value in twentyToThirty]
print(twentyToThirty)

# 4-7
print(ranNumbers[0:2])
print(ranNumbers[4:10])
print(ranNumbers[16:21])

# 4-8
favMusicians = ["The chainsmokers","Blink-182", "The weeknd"]
favBands = favMusicians[:]
favMusicians.append("Maroon 5")
print(favMusicians)
print(favBands)

#4-9
schoolGrades = ("1st", "2nd", "3rd", "4th", "5th")
schoolGrades[0] = "1s"
