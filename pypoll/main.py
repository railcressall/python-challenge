import csv

# Path to your CSV file

csv_file_path = r"C:\Users\railc\OneDrive\Desktop\python-challenge\pypoll\resources\election_data.csv"

# Open the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)


# Variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# CSV reader 
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip header
    header = next(csv_reader)

    # Each row in the CSV file
    for row in csv_reader:
        candidate = row[2]

        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        # Update the winner information
        if candidates[candidate] > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = candidates[candidate]

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Print the analysis to the terminal
analysis_results = (
    "Election Results\n"
    "----------------------------\n"
    f"Total Votes: {total_votes}\n"
    "----------------------------\n"
)

# Each candidate and print their results
for candidate, votes in candidates.items():
    percentage = percentages[candidate]
    analysis_results += f"{candidate}: {percentage:.2f}% ({votes})\n"

analysis_results += (
    "----------------------------\n"
    f"Winner: {winner['name']}\n"
    "----------------------------\n"
)

print(analysis_results)

# Export the results to a text file

output_file_path = r"C:\Users\railc\OneDrive\Desktop\python-challenge\pypoll\analysis\analysis.txt"


with open(output_file_path, 'w') as output_file:
    output_file.write(analysis_results)

print(f"\nAnalysis results exported to: {output_file_path}")