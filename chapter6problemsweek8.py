#problem 6-1
#declare dictionary for the new doctor strange movie 
doctorStrangeMovie = {"Movie_Title": "Doctor Strange in the Multiverse of Madness", 
                "movie_rating": "PG-13", 
                "director": "Sam Raimi",  
                "year_released" : 2022, 
                "writer" : "Michael Waldron", 
                "user_rating" : "7.4/10"}

# problem 6-2
# declare dictionary 
hpEnvy = {"Item Number": 4156, 
        "Product Name" : "HP Envy", 
        "Price" : 1050}

# multiple price by 1.30
hpEnvy["Price"] *= 1.30

#display price
print(f"{hpEnvy['Product Name']}'s price has been increased to ${hpEnvy['Price']}")

#problem 6-3
# declare for loop to loop through the items in hp envy
for key, value in hpEnvy.items():
    print(f"{key} {value}")

#Problem 6-4
# declare dictionary
dictionary = [{"Word" : "Meditation", "Definition" : "An altered state of consiciousness of being mentally aware"},
{"Word" : "Mindfulness", "Defintion" :"The process of being mentally aware outside the session"}, 
{"Word" : "Python", "Definition" : "A programming language that I will be using for a few classes here at Walsh College"}]

# declare increment variable 
count = 0 

#start for loop to display items in a dictionary
for word in dictionary:
    for key, value in dictionary[count].items():
        print(f"{key} {value}")
    count += 1

# problem 6-5
doctorStrangeMovie = {"Movie_Title": "Doctor Strange in the Multiverse of Madness", 
                    "movie_rating": "PG-13", 
                    "director": "Sam Raimi",  
                    "year_released" : 2022, 
                    "writer" : "Michael Waldron", 
                    "user_rating" : "7.4/10", 
                    "Actors/Actresses": ["Benedict Cumberbatch", "Elizabeth Olsen", "Chiwetel Ejiofor", "Xochitl Gomez"]}

for actor in doctorStrangeMovie["Actors/Actresses"]:
    print(actor)