import re
import sys
from datetime import date

# Basic Python script to parse Technical call CSV and provide per-person breakdowns
# Takes in latest "Performance Overview" CSV and outputs a CSV with easily broken down call volume
# Parses CSV, going line by line to find 'VSP Tech Support' and then collating all data after that point

regexp_inside = '.*Answered.*'
regexp_outside = '.*Total:.*'
regexp_queuelist = '.*Tech.*'

queuelist_total = {'8201 - VSP Tech Support':0, '8222 - UPSONIC Technical Support':0, '8302 - VSP Tech Support':0, '8401 - VSP Tech Support':0, '8602 - VSP Tech Support':0, '9900 - Sales to VSP Tech Support':0}
queuelist_answered = {'8201 - VSP Tech Support':0, '8222 - UPSONIC Technical Support':0, '8302 - VSP Tech Support':0, '8401 - VSP Tech Support':0, '8602 - VSP Tech Support':0, '9900 - Sales to VSP Tech Support':0}

#Bring in filename from drag + drop
filename = sys.argv[1:][0]

with open(filename, mode='r') as file:
    #Using this variable to track whether we are inside a VSP Tech Support call queue
    writedata = bool(0)
    
    for line in file:
        if re.match(regexp_inside, line):
            #We have hit the queue results
            writedata = bool(1)
            
        elif re.match(regexp_outside, line):
            #We have hit EOF
            writedata = bool(0)
              
        else:
            #Check if we are inside the queue
            if writedata:
                #We are inside the queue results
                if re.match(regexp_queuelist, line): #Match to ensure we are looking at a tech queue
                    #Add call quantity to total
                    queuelist_total[line.split(",")[0]] += int(line.split(",")[2])
                    #Add call quantity to answered
                    queuelist_answered[line.split(",")[0]] += int(line.split(",")[4])

with open("Call Totals " + date.today().strftime("%b-%d-%Y") + ".csv", "x") as writefile:
    #Open our output CSV
    writefile.write("Queue Name,Total Calls,Answered Calls\n")
    for queue in queuelist_total:
        #Write File with Queue Name + , + queue calls taken + newline
        writefile.write(queue + "," + str(queuelist_total[queue]) + "," + str(queuelist_answered[queue]) + "\n")

print("Results written to CSV File. Printing results below..")
for key in queuelist_total:
    print(key)
    print("Total: " + str(queuelist_total[key]))
    print("Answered: " + str(queuelist_answered[key]))

totalcalls = 0
totalanswered = 0

#Add all calls for a total
for key in queuelist_total:
    totalcalls += int(queuelist_total[key])
    totalanswered += int(queuelist_answered[key])

print ("TOTAL CALLS: " + str(totalcalls))
print ("TOTAL ANSWERED: " + str(totalanswered))
input()
