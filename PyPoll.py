#Data needed
# total votes cast
# List of Candidattes
# Percentage for each can
# Total for each Can
# winner based on pop vote

import csv
import os 

#Assign variable to hold data file path
file_load = os.path.join('Resources','election_results.csv')

#Assign variable to hold analysis file path
file_save = os.path.join("Analysis","election_analysis.txt")

#initialize a total vote counter
total_votes = 0 
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open(file_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")



#open election results and read file
with open(file_load) as election_data:
    file_reader = csv.reader(election_data)

    #print header row 
    headers = next(file_reader)
    
    for row in file_reader:

        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            
            #add candidate to list
            candidate_options.append(candidate_name)

            #Track candidates votes 
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        

        
        
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes)/float(total_votes) * 100

        formatted_vote_percentage = "{:.1f}".format(vote_percentage)

        #determine winning candidate
        # check if votes are greater than winning count/percent
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
           
            winning_percentage = vote_percentage

            winning_candidate = candidate_name



        print(f"{candidate_name}: {formatted_vote_percentage}% ({votes:,})\n")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
        
print(total_votes)









election_data.close()


