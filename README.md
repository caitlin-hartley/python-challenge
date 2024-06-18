# python-challenge

# ---------------------------------------------------------------------------------
# First Challenge Overview:

# Python script to analyze the financial records of company

#Calculates:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period

# ---------------------------------------------------------------------------------

# First Challenge Script Description:

# Imports csv file and creates variables and lists to use in script

# Iterates through the rows of the csv file to: 
    # Calculate the total months by adding each row in csv file 
    # Calculates the total profit/loss by casting column 2 as an integer and summing across rows
    # Create lists of values in both columns

# Iterates through profit/loss list to calculate the revenue change by subtracting row from previous row in Profit/Loss column; appens to revenue change list

# Calculates the average change in revenue by dividing the sum of the changes in revenue by the length of the list (Number of times the revenue changes)

# Calculates the greatest increase in revenue by finding the max value in the revenue change list

# Calculates the greatest decrease in revenue by finding the min value in the revenue change list

# Finds the month with the greatest increase by finding the index number of the greatest increase and subtracting 1 in the months list

# Finds the month with the greatest decrease by finding the index number of the greatest decrease and subtracting 1 in the months list

# Prints results using f strings; formats revenue_average to have 2 decimal places

# Writes results to output file

# ---------------------------------------------------------------------------------
