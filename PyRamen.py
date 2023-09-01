import csv
#File to load and output

file_to_load ="menu_data.csv
file_to_load = "sales_data.csv"
file_to_output = "menu_data.txt"
file_to_output = "sales_data.csv"

#Track Menu and Sales Data 
menu = []
sales = []

# Open and read the csv 
with open (Resources/menu_data.csv_path, ="") as menu_csv
    reader = csv.reader (menu.csv=",")
    next(menu)
    for item in menu:
    menu_list.append(item)
    
with open (Resources/sale_data.cvs_path, ="") as sales_data.csv
    reader = csv.reader (sales_data.csv)
    next(sales)
    for revenue in sales
    sale_list.append(revenue)
    
   
   
   
   
   
   
   
   
   
   
# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# -->>  Export a text file with the results
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")
#Print the Output
print(file_to_output)

#Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(file_to_output)