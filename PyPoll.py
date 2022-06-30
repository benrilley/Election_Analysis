import csv
import os
from wsgiref import headers
file_to_load = os.path.join('Resources', 'election_results.csv') 
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "Election_Analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

 # Write some data to the file. 
    txt_file.write("Arapahoe\nDenver\nJefferson") 
    # Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    file_reader = csv.reader(election_data) 
    # Print each row in the CSV file.
    #for row in file_reader:
       # print(row)
       # Print header row
    headers= next(file_reader)
    print(headers)
