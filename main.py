import csv

filename = str(input("Enter File Name\n"))

file_CSV = open(filename)
data_CSV = csv.reader(file_CSV)
list_CSV = list(data_CSV)
 

states = []
stateWise = {}
total = 0

for i, row in enumerate(list_CSV):
    if(i==0):
        continue

    state = row[4]
    amount = row[7]

    if state not in states:
        states.append(state)

    try:
        stateWise[state]
    except KeyError:
        stateWise[state] = 0.00
    
    stateWise[state] += float(amount)
    total += float(amount)


with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 

    csvwriter.writerow(["State", "Amount", "Tax"])
    for key,value in stateWise.items():
        try:
            csvwriter.writerow([str(key), str(round(value, 2)), str(round(value*5/100, 2))])
        except KeyError:
            print("Ignoring State" + key)

print(total)