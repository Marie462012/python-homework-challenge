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
    
    for row in reader:

#Track the totals

total_months = total_months + 1
total_pl = total_pl +int(firstrow[1])
value =int(first_row[1])

#Track revenue changes
revenue_change =int(row["Revenue]") - prev_revenue
prev_revenue = int(row["Revenue"])
revenue_change_list = revenue_change_list + [revenue_change]
month_of_change =month_of_change = [row["Date"]]

#Calculate the greatest increase
if (revenue_change > greatest_increase[1]):
    greatest_increase[0] = row["Date"]
    greatest_increase[1] = revenue_change

#Calculate the greatest decrease
if (revenue_change < greatest_decrease [1]):
    greatest_decrease[0] = row["Date"]
    greatest_decrease[1] = revenue_change
    
#Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
  
#Generate Output Summary
output = (
    f"\nFinancialAnalysis\n"
    f"--------------------\n"
    f"total_months: {total_months}\n"
    f"total revenue: ${total revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} ($[greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: [greatest_decrease[0]} ($[greatest_decrease[1])"\n"
    

#Print the Output
print(file_to_output)

#Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(file_to_output)