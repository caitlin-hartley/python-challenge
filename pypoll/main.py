# Python script that analyzes the votes and calculates each of the following values:

    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

# Module to import file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for csv file
csv_path=os.path.join('resources', 'election_data.csv')

# Create total votes variable and set to 0
total_votes = 0

# Create candidates list 
candidates = []

# Create dictionary for number of votes for each candidate
number_of_votes = {}

# Create list for vote percentages
vote_percentages =[]

# Open csv file
with open(csv_path) as csv_file:

    # Read csv file
    election_csv = csv.reader(csv_file, delimiter=',')

    # Read the header row first
    csv_header=next(election_csv)

    # Create loop to iterate through rows of csv file
    for row in election_csv: 

        # Count total number of votes
        total_votes +=1

        # Create list of unique candidates 
        if row[2] not in candidates:
            candidates.append(row[2])

            # Set candidate vote dictionary to 0 for each unique candidate (resets)
            number_of_votes[row[2]] = 0
        
        # Sum votes for each candidate
        number_of_votes[row[2]] += 1

# Split dictionary into candidate name and vote count
candidate, vote_count = zip(*number_of_votes.items())

# Calculate percentage of votes for each candidate
for i in vote_count:
    percent = i/total_votes *100
    vote_percentages.append("%.3f" % percent)

# Calculate winner with max number of votes
winner = candidate[vote_count.index(max(vote_count))]

# Print results into terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for i in range(3):
    print(f'{candidate[i]}: {vote_percentages[i]}% ({vote_count[i]})')

print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# Open text file
with open(os.path.join('analysis','output.txt'), 'w') as output_file:
    # Write results to text file
    output_file.write('Election Results\n')
    output_file.write('-------------------------\n')
    output_file.write(f'Total Votes: {total_votes}\n')
    output_file.write('-------------------------\n')
    for i in range(3):
        output_file.write(f'{candidate[i]}: {vote_percentages[i]}% ({vote_count[i]})\n')
    output_file.write('-------------------------\n')
    output_file.write(f'Winner: {winner}\n')
    output_file.write('-------------------------\n')
