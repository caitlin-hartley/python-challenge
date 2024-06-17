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

# Set path for csv file
csv_path=os.path.join('resources', 'budget_data.csv')

# Create total months variable and set to 0
total = 0

# Create net profit/loss variable
net = 0

# Create profit/loss list
profit_loss = []

# Create revenue change list
revenue_change = []

# Create months list
months = []

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

        # Append months list with Date column values
        months.append(str(row[0]))

    # Create loop to iterate through profit/loss list
    for i in range (1, len(profit_loss)):

        # Calculate revenue change as row - previous row
        revenue_change.append((int(profit_loss[i]) - (int(profit_loss[i-1]))))
    
    # Calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)

    # Calculate greatest increase in revenue
    greatest_increase = max(revenue_change)

    # Calculate greatest decrease in revenue
    greatest_decrease = min(revenue_change)

    # Calculate month with greatest increase
    month_increase = months[revenue_change.index(max(revenue_change))+1]

    # Calculate month with greatest decrease
    month_decrease = months[revenue_change.index(min(revenue_change))+1]

# Print results into terminal
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total}')
print(f'Total: ${net}')
print(f'Average Change: ${"%.2f" % revenue_average}')
print(f'Greatest Increase in Profits: {month_increase} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})')

# Open text file
with open(os.path.join('analysis','output.txt'), 'w') as output_file:
    # Write results to text file
    output_file.write("Financial Analysis\n" )
    output_file.write("----------------------------\n")
    output_file.write(f'Total Months: {total}\n')
    output_file.write(f'Total: ${net}\n')
    output_file.write(f'Average Change: ${"%.2f" % revenue_average}\n')
    output_file.write(f'Greatest Increase in Profits: {month_increase} (${greatest_increase})\n')
    output_file.write(f'Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})\n')
