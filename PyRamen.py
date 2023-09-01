import csv

#File to load and output
file_to_load = "menu_data.csv"
file_to_load = "sales_data.csv"
file_to_output = "menu_data.txt"
file_to_output = "sales_data.csv"

#Track Menu and Sales Data 
menu = []
sales = []
report = []


# Open and read the csv 
with open (Resources/menu_data.csv_path, ="") as menu_csv
    reader = csv.reader (menu.csv=",")
    next(menu)
    for item in menu:
    menu_list.append(item)
    for row in menu
    for row[row]] = {
        "price":float (row[3]),
        "cost" : float (row [4])
    
     
with open (Resources/sale_data.cvs_path, ="") as sales_data.csv
    reader = csv.reader (sales_data.csv)
    next(sales)
    for revenue in sales
    sale_list.append(revenue)
    for row in sales
    sales[row[0]] = {
        "Quantity" int(int(row{3}))
        "Menu_item" int(row {4})
        
          if row[4] not in report:
            report[row[4]] = {
                "01-count": 0,
                "02-revenue": 0,
                "03-cogs": 0,
                "04-profit": 0,
                }
    
   or sales_item in sales.values():
    match = 0
    for item_on_menu, price_cost in menu.items():
        if  sales_item["Menu_item"] == item_on_menu:
            report[sales_item["Menu_item"]]["01-count"] += sales_item["Quantity"]
            report[sales_item["Menu_item"]]["02-revenue"] += price_cost["price"] * sales_item["Quantity"]
            report[sales_item["Menu_item"]]["03-cogs"] += price_cost['cost'] * sales_item["Quantity"]
            report[sales_item["Menu_item"]]["04-profit"] = report[sales_item["Menu_item"]]["02-revenue"] - report[sales_item["Menu_item"]]["03-cogs"]
            match = 1
    if match == 0:
        print(f"{sales_item} does not equal any item! NO MATCH!") 

print(report) 


#Print the Output
print(file_to_output)

#Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(file_to_output)




#Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(file_to_output)
