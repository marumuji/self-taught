import csv

titleList = [["Top Gun", "Risky Business", "Minority Report"],
            ["Titanic", "The Revenant", "Inception"],
            ["Training day", "Man on Fire", "Flight"]]

print(titleList)

with open("movieTitle.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for row in titleList:
        w.writerow(row)