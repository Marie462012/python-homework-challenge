import csv

#File to load and output

file_to_load ="budget_data_1.csv"
file_to_output = "budget_data_1.txt"

#Track various budget parameters
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

# Open and read the csv and convert into a list of dictionaries
with open(file_to_load) as budget_data:
    reader =csv.DictReader(budget_data)

#Track the totals

total_months = total_months + 1
total_pl = total_pl +int(firstrow[1])
value =int(first_row[1])

#First Row of Data 
for row in csvreader

#Keeping track of the dates
dates.append(row[0])

