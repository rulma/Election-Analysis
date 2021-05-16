#Data needed
# total votes cast
# List of Candidattes
# Percentage for each can
# Total for each Can
# winner based on pop vote

import csv
import os 

#Assign variable to hold data file path
file_load = os.path.join('Resources','election_results.xls.csv')

#Assign variable to hold analysis file path
file_save = os.path.join("Analysis","election_analysis.txt")

with open(file_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")



#open election results and read file
with open(file_load) as election_data:
    file_reader = csv.reader(election_data)

    #print header row 
    headers = next(file_reader)
    print(headers)

    # for row in file_reader:
    #     print(row[0])









election_data.close()


