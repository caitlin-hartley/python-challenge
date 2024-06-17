# Python script to analyze the financial records of company

#Calculates:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period



# Module to import file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csv_path=os.path.join('resources', 'budget_data.csv')

# Create total months variable and set to 0
total = 0

# Create net profit/loss variable
net = 0

# Create profit/loss list
profit_loss = []

# Create revenue change list
revenue_change = []

# Open csv file
with open(csv_path) as csv_file:

    # Read csv file
    budget_csv = csv.reader(csv_file, delimiter=',')

    # Read the header row first
    csv_header=next(budget_csv)

    # Create loop to iterate through rows of csv file
    for row in budget_csv: 
        
        # Count total number of months
        total +=1

        # Calculate net profit/loss
        net = net + int(row[1])

        # Append profit/loss list with Profit/Loss column values
        profit_loss.append(int(row[1]))

    # Create loop to iterate through profit/loss list
    for i in range (1, len(profit_loss)):

        # Calculate revenue change as row - previous row
        revenue_change.append((int(profit_loss[i]) - (int(profit_loss[i-1]))))
    
    # Calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)

    print(total)
    print(net)
    print("%.2f" % revenue_average)
    #print(revenue_change)
    #print(len(revenue_change))