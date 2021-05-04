# one = 5 + 2 * 3
# two = 8 // 5 - 3
# three =8 + 22 * 2 - 4
# four = 16 - 3 / 2 + 7 - 1
# five = 3 ** 3 % 5
# six = 5 + 9 * 3 / 2 - 4

# print(one)
# print(two)
# print(three)
# print(four)
# print(five)
# print(six)

# counties = ["Fairfax","Santa Cruz", "Hermosa"]
# print(counties)
# user_county = ""

# user_county = input("What County do you live in? ")
# counties.append(user_county+"ab")

# print(counties)

# user_fix = input("Oh no I mispelled your county. Can you reenter it for me? ")
# counties[3] = user_fix
# print(counties)

# my_dictionary = {}
# user_word = input("Give me a word: ")

# user_definition = input("Now define that word: ")
# my_dictionary[user_word] = user_definition
# print(my_dictionary)
# print(my_dictionary.keys())

#create empty voting data dictionary
voting_data = []

#add voting data to dictionary
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#take a user input 3 times to add to dataset
for x in range(3):
    counties_added = input(f"Give county name: ")
    counties_vote = input(f"Total Votes: ")
    voting_data.append({"county":counties_added,"registered_voters":counties_vote})


#print intial dictionary
print(voting_data)

#prompt user to include el paso or not"
if input("is El Paso in your state? ") == "yes":
#insert El Paso into second index in voting data dict
    voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})



#print updated dictionary
    print(voting_data)

#do not update dictionary and add user input
else:
    voting_data.append({"county":counties_added,"registered_voters":counties_vote})
    print(voting_data)
