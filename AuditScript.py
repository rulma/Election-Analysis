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
