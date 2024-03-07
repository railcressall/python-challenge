import csv

# Specify the path to your CSV file
csv_file_path = '\budget_data.csv'

# Open the CSV file and read its content
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        print(row)



