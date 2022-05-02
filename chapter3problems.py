#3-1
from math import factorial
from stat import FILE_ATTRIBUTE_ARCHIVE


walshBooks =["Python Crash course", "Server+", "Security+,", "System Analysis and Design"]
print("I just read: " + walshBooks[0])
print("I just read: " + walshBooks[1])
print("I just read: " + walshBooks[2])
print("I just read: " + walshBooks[3])

#3-2
favTvShows = ["Blacklist", "The flash", "Quantico", "Supergirl"]
favTvShows.remove("The flash")
favTvShows.append("House")
favTvShows.append("The walking dead")
favTvShows.insert(2, "Supernatural")
walkingDead = favTvShows.pop(-1)
print(walkingDead)
del favTvShows[0:3]
print(favTvShows)

#3-3
favAmusementParks = ["Cedar Point", "Kings Island", "Carowinds", "Dollywood"]
print(len(favAmusementParks))
favAmusementParks.sort()
print(favAmusementParks)
favAmusementParks.reverse()
print(favAmusementParks)
print(sorted(favAmusementParks))

#3-4 
evenNumbers = [2,4,6,8,10]

print(evenNumbers[5])
# evenNumbers = [2,4,6,8,10,12]
#
# print(evenNumbers[5])
