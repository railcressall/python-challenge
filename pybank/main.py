import csv


csv_file_path = r"C:\Users\railc\OneDrive\Desktop\python-challenge\pybank\resources\budget_data.csv"


with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)



total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}


with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

  
    header = next(csv_reader)

   
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])

      
        total_months += 1
        net_total += profit_loss


        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        previous_profit_loss = profit_loss


average_change = sum(changes) / len(changes)


analysis_results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
)

print(analysis_results)



output_file_path = r"C:\Users\railc\OneDrive\Desktop\python-challenge\pybank\analysis\Financial_analysis.txt"

with open(output_file_path, 'w') as output_file:
    output_file.write(analysis_results)




print(f"\nAnalysis results exported to: {output_file_path}")
