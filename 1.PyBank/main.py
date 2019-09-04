# Dependencies
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skipping the header row.
    next(csvreader, None)

    monthcount = 0
    ProfitLoss = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
    Sumchange = 0
    Count = 0
    Avgchange = 0
    storevalue = 0

    for row in csvreader:
        monthcount += 1
        ProfitLoss +=  int(row[1])
        if storevalue != 0:
            Avgchange = int(row[1]) - storevalue
            Sumchange += Avgchange
            Count += 1

        if Avgchange > GreatestIncrease:
            GreatestIncrease = Avgchange
            GreatIncDate = row [0]
        if Avgchange < GreatestDecrease:
            GreatestDecrease = Avgchange
            GreatDecDate = row [0]
        storevalue = int(row[1])

    AveragePL = Sumchange / Count
    AveragePL = float("{0:.2f}".format(AveragePL))

    # Specify the file to write to
    output_path = os.path.join("results.csv")
    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')
        # Write the first row (column headers)
        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow(["------------------------------------------"])
        csvwriter.writerow([f"Total months included in the analysis:  {monthcount}"])
        csvwriter.writerow([f"Total (profit or loss):  {ProfitLoss}"])
        csvwriter.writerow([f"Average change: {AveragePL}"])
        csvwriter.writerow([f"Greatest increase in profits: {GreatIncDate} ($ {GreatestIncrease})"])
        csvwriter.writerow([f"Greatest decrease in profits: {GreatDecDate} ($ {GreatestDecrease})"])

    print("")
    print("Financial Analysis")
    print("------------------------------------------")
    print(f"Total months included in the analysis: {monthcount}")
    print(f"Total (profit or loss):  {ProfitLoss}")
    print(f"Average change: {AveragePL}")
    print(f"Greatest increase in profits: {GreatIncDate} ($ {GreatestIncrease})")
    print(f"Greatest decrease in profits: {GreatDecDate} ($ {GreatestDecrease})")



