"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

Excessively commented because that's the point!
"""

#create a blank dictionary to hold sales data, keyed by salesperson
sales_data = {}
# salespeople = []
# melons_sold = []

#open the sales report file for reading
sales_report_file = open("sales-report.txt")

#iterate through the file entry by entry (line by line), updating overall
#sales data (sales_data dictionary) with that line's data
for line in sales_report_file:

    #pull whitespace off the end of the line
    line = line.rstrip()

    #split the line at each pipe, put the entries into the entries list
    entries = line.split("|")

    #get the name of the salesperson, the total sale, and the number of
    #melons sold
    salesperson = entries[0]
    total_sale = float(entries[1])
    melons = int(entries[2])

    #search for salesperson in sales_data dictionary
    #if found, update total sales and melon total
    if salesperson in sales_data:
        sales_data[salesperson]["total sales"] += total_sale
        sales_data[salesperson]["total melons sold"] += melons

    #if salesperson isn't in sales_data dictionary, add a new entry with that
    #person's info
    else:
        sales_data[salesperson] = {"total sales": total_sale,
                                   "total melons sold": melons}


#QUESTION: DIFFERENCE BETWEEN USING KEY TO REFER TO JUST THE KEY AND USING KEY
#TO REFER TO ITS VALUE (FEELS LIKE I'M DOING A LOT OF DEREFERENCING)

#go through sales data and print info for each sales person
for salesperson in sales_data:
    #get data for current salesperson
    melons = sales_data[salesperson]["total melons sold"]
    sales = sales_data[salesperson]["total sales"]

    #create and print string describing current salesperson's sales
    outstr = "{name} sold {num_melons} melons for a total of ${gross:,.2f}"
    print outstr.format(name=salesperson, num_melons=melons, gross=sales)
