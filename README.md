# python-challenge

# ----------------------------------------------------------------------
# First Challenge Overview:

    # Python script to analyze the financial records of company

    # Calculates:
        # The total number of months included in the dataset
        # The net total amount of "Profit/Losses" over the entire period
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in profits (date and amount) over the entire period

        # Credit to stack overflow for helping to find row - previous row calculation
        # Credit to stack overflow to use another values index to find value in another list
        
# ----------------------------------------------------------------------

# First Challenge Script Description:

    # Imports csv file and creates variables and lists to use in script

    # Iterates through the rows of the csv file to: 
        # Calculate the total months by adding each row in csv file 
        # Calculates the total profit/loss by casting column 2 as an integer and summing across rows
        # Create lists of values in both columns

    # Iterates through profit/loss list to calculate the revenue change by subtracting row from previous row in Profit/Loss column; appends to revenue change list

    # Calculates the average change in revenue by dividing the sum of the changes in revenue by the length of the list (Number of times the revenue changes)

    # Calculates the greatest increase in revenue by finding the max value in the revenue change list

    # Calculates the greatest decrease in revenue by finding the min value in the revenue change list

    # Finds the month with the greatest increase by finding the index number of the greatest increase and subtracting 1 in the months list

    # Finds the month with the greatest decrease by finding the index number of the greatest decrease and subtracting 1 in the months list

    # Prints results using f strings; formats revenue_average to have 2 decimal places

    # Writes results to output file

# ----------------------------------------------------------------------

# Second Challenge Overview:

    # Python script to analyze the financial records of company

    # Python script that analyzes the votes and calculates each of the following values:
        # The total number of votes cast
        # A complete list of candidates who received votes
        # The percentage of votes each candidate won
        # The total number of votes each candidate won
        # The winner of the election based on popular vote

        # Credit to stack overflow for helping to calculate values based on list of keys for dictionary
        # Credit to stack overflow for helping to split dictionary into two lists using zip

# ----------------------------------------------------------------------

# Second Challenge Script Description:

    # Imports csv file and creates variables, lists, and dictionaries to use in script

    # Iterates through the rows of the csv file to: 
        # Calculate the total votes by adding each row in csv file 
        # Create unique candidate list
        # Create dictionary with unique candidate names and vote counts for each candidate

    # Splits dictionary into unique lists of candidate name and voter count

    # Calculates percent votes by taking each value in vote count and divinding by the total number of votes

    # Finds the winner by finding the candiate name based on the index of vote count list with greatest amount of votes

    # Prints results using f strings; iterates through three lists (candidate name, percentage of votes, and vote count) to print results for each candidate

    # Writes results to output file

# ----------------------------------------------------------------------

