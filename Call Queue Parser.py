import re
import sys
from datetime import date

# Basic Python script to parse Technical call CSV and provide per-person breakdowns
# Takes in latest "Performance Overview" CSV and outputs a CSV with easily broken down call volume
# Parses CSV, going line by line to find 'VSP Tech Support' and then collating all data after that point

regexp_techline = '.*VSP Tech Support.*'
stafflist = {'Jim Tsacalos': 0, 'Ben Johnson': 0, 'Jacob El-Chami': 0, 'Patrick Ng': 0, 'Paul Kilpatrick': 0, 'Justin Pantalleresco': 0, 'Bryce Mackay': 0, 'Tech Support': 0, 'Glenn Hayes': 0, 'Tom Wood': 0, 'Yuvy Iyer': 0}

#Bring in filename from drag + drop
filename = sys.argv[1:][0]

with open(filename, mode='r') as file:
    #Iterate through the CSV lines
    for line in file:
        #Check if this line relates to the Tech Queue
        if re.match(regexp_techline, line):
            #This is a tech queue line
            stafflist[line.split(",")[1]] += int(line.split(",")[5])

with open("Tech Queue " + date.today().strftime("%b-%d-%Y") + ".csv", "x") as writefile:
    #Open our output CSV
    for staff in stafflist:
        #Write File with Staff Name + , + staff calls taken + newline
        writefile.write(staff + "," + str(stafflist[staff]) + "\n")
        #Print for easy access
        print(staff + " took " + str(stafflist[staff]) + " calls.")
input()
