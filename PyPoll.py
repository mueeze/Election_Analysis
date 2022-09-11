#The data we need to retrieve..
# 1. The total number of votes cast. 
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

import csv
from distutils.text_file import TextFile
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
#Print each row in the CSV file
    #for row in file_reader:
        #print(row)
#Read and print the header row
    headers = next(file_reader)
    print(headers)

import os

#Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, 'w') as txt_file:

# Write 3 counties to the file.
    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")

# To do: perform analysis.
# Read and analyze the data here.
#Read the file object with the reader function. 
    


    



# Close the file.