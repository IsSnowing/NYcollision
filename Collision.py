import csv
import pprint
import numpy as np
import matplotlib.pyplot as plt

def clean(readfile, writefile):
    variables = ["ZIP CODE", "NUMBER OF PERSONS INJURED", "NUMBER OF PERSONS KILLED"]
    data = []
    with open(readfile, 'r', newline='', encoding='utf-8-sig') as csvfile:
        csvfile_write = open(writefile, 'w', newline='', encoding='utf-8-sig')
        writer = csv.DictWriter(csvfile_write, fieldnames=variables)
        writer.writeheader()
        reader = csv.DictReader(csvfile)
        for row in reader:
            ZIP = row['ZIP CODE']
            INJURED = row['NUMBER OF PERSONS INJURED']
            KILLED = row['NUMBER OF PERSONS KILLED']

            writer.writerow(
                {'ZIP CODE': ZIP, 'NUMBER OF PERSONS INJURED': INJURED, 'NUMBER OF PERSONS KILLED': KILLED})
        csvfile.close()
    print("finish cleaning!!!!!!!")

def readcsv(filename):
    print("reading.....")
    #col in the csv file, all the attributes
    variables = ["DATE", "TIME", "NUMBER OF PERSONS INJURED", "NUMBER OF PERSONS KILLED"]
    #stores the rest of the info
    data = [[]]*len(variables)

    #initial the data with empty list to store the data for each variable
    #for var_index in range(0, len(variables)):
     #   data.append([])

    #open the file
    for variable in range(0, len(variables)):
        data[variable] = []

    with open(filename, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        #reader = csv.DictReader(open("people.csv"))
        for row in reader:
            for var_index in range(0, len(variables)):
                #store the info in to data row by row, varaiables[var_index] == col in the csv files
                data[var_index].append(row[variables[var_index]])

        csvfile.close()

    return data, variables

def time_vs_x(time, injured, killed):
    lst_time = []
    injures = []
    kills = []
    for i in range(0, 24):
        lst_time.append([i])
        injures.append(0)
        kills.append(0)


    for t in range(0, len(time)):
        slice = time[t].index(':')
        hour = int(time[t][0:slice])
        injures[hour] += int(injured[t])
        kills[hour] += int(killed[t])

    sum = 0
    sum1 = 0
    for kill in kills:
        sum += kill

    for injure in injures:
        sum1 += injure
    print(sum)
    print(sum1)

    plt.xlim([0, 24])
    #plt.ylim([0, 100])
    plt.xticks(np.arange(0, 24, 1))
    # plt.ylim([-3, 3])
    plt.plot(lst_time, injures, kills)
    plt.show()

    #return lst_time, injures, kills

def locations_vs_x(location, injured, killed):
    lst_loc = []
    injures = []
    kills = []
    for i in range(0, 24):
        lst_loc.append([i])
        injures.append(0)
        kills.append(0)


    for t in range(0, len(location)):
        slice = location[t].index(':')
        hour = int(location[t][0:slice])
        injures[hour] += int(injured[t])
        kills[hour] += int(killed[t])

    sum = 0
    sum1 = 0
    for kill in kills:
        sum += kill

    for injure in injures:
        sum1 += injure
    print(sum)
    print(sum1)

    plt.xlim([0, 24])
    #plt.ylim([0, 100])
    plt.xticks(np.arange(0, 24, 1))
    # plt.ylim([-3, 3])
    plt.plot(lst_time, injures, kills)
    plt.show()

def main():
    clean("NYPD_Motor_Vehicle_Collisions.csv", "Location_collisions.csv")
    #data, variables = readcsv("Date_time_collisions.csv")
    print("ploting.....")
    #time_vs_x(data[1], data[2], data[3])


    #pprint.pprint(data)

main()