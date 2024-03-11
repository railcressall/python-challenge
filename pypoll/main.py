import csv


csv_file_path = r"C:\Users\railc\OneDrive\Desktop\python-challenge\pypoll\resources\election_data.csv"


with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)



total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}


with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    
    header = next(csv_reader)


    for row in csv_reader:
        candidate = row[2]

       
        total_votes += 1

      
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        
        if candidates[candidate] > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = candidates[candidate]


percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}


analysis_results = (
    "Election Results\n"
    "----------------------------\n"
    f"Total Votes: {total_votes}\n"
    "----------------------------\n"
)


for candidate, votes in candidates.items():
    percentage = percentages[candidate]
    analysis_results += f"{candidate}: {percentage:.2f}% ({votes})\n"

analysis_results += (
    "----------------------------\n"
    f"Winner: {winner['name']}\n"
    "----------------------------\n"
)

print(analysis_results)



output_file_path = r"C:\Users\railc\OneDrive\Desktop\python-challenge\pypoll\analysis\analysis.txt"


with open(output_file_path, 'w') as output_file:
    output_file.write(analysis_results)

print(f"\nAnalysis results exported to: {output_file_path}")
