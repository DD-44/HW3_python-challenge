# Dependencies
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skipping the header row.
    next(csvreader, None)

    Names = []
    Votes = []
    Percent = []

    for row in csvreader:
        x = row[2]
        index=None
        NameCheck = False
        for name in Names:
           if name == x:
                NameCheck = True
        
        if NameCheck == True:
            index = Names.index(x)
            Votes[index] += 1
        else:
            Names.append(x)
            Votes.append(1)

    CountVotes = sum(Votes) 
    for n in Votes:
        P = n/CountVotes
        P2 = "{:.2%}".format(P)
        Percent.append(P2)
    MaxVotes = max(Votes)
    index2 = Votes.index(MaxVotes)
    Winner = Names[index2]

    Lenght = int(len(Votes))

    # Specify the file to write to
    output_path = os.path.join("results_PyPoll.csv")
    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')
        # Write the first row (column headers)
        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["------------------------------------------"])
        csvwriter.writerow([f"Total votes:  {CountVotes}"])
        csvwriter.writerow(["------------------------------------------"])
        for i in range(Lenght):
            csvwriter.writerow([f"{Names[i]}:   {Percent[i]}  ({Votes[i]})"])
        csvwriter.writerow(["------------------------------------------"])
        csvwriter.writerow([f"Winner:  {Winner}"])
        csvwriter.writerow(["------------------------------------------"])


    print("")
    print("Election Results")
    print("------------------------------------------")
    print(f"Total votes:  {CountVotes}")
    print("------------------------------------------")
    for i in range(Lenght):
        print(f"{Names[i]}:  {Percent[i]}  ({Votes[i]})")
    print("------------------------------------------")
    print(f"Winner:  {Winner}")
    print("------------------------------------------")
    
 

