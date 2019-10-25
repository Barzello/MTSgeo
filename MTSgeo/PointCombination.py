#coding: UTF-8
#!/bin/env python3
import pandas as pd
import math
import csv


# data = pd.read_csv("~/Programming/HackMoscow/Data/inputs.csv")
def checkPointInRaduis(point1, point2, radius):
    try:
        # For debigging
        print(" Distance {0} and radius {1}".format(math.sqrt(pow( point1['lat'] - point2['lat'], 2) +
            pow( point1['lon'] - point2['lon'] , 2)), float(radius) ))

        return math.sqrt( pow(point1['lat'] - point2['lat'] , 2) +
            pow( point1['lon'] - point2['lon'], 2) ) < float(radius)
    except:
        return False # If the input row paramets is string

def LinkPoints(row, index):
    fewPoints = []
    j = index - 1 # Removing checking the same numbers
    try:
        while(checkPointInRaduis(row[index], row[j], row[index]['radius'])):
            fewPoints.append(row[j])
            j-=1
    except:
        return [row[index + 1]] # if Index is out of range -

    j = index + 1 # Removing checking the same numbers
    try:
        # check points after
        while(checkPointInRaduis(row[index], row[j], row[index]['radius'])):
            fewPoints.append(row[j])
            j+=1
    except:
        return [row[index - 1]] # if Index is out of range -
    print("Linked points is : {0}".format(fewPoints))
    return fewPoints


if __name__ == '__main__':
    data = csv.DictReader(
        open("/home/ristle/Programming/HackMoscow/Data/inputs.csv"))
    dict = []

    # coef for conversation betwen lat and lon to metres
    linLon2M =  111321.377778

    for row in data:
        row['lat'] = math.cos(float(row['lat'])) * linLon2M
        row['lon'] = math.cos(float(row['lon'])) * linLon2M
        dict.append(row)

    i = 0
    for row in dict:
        linkedPoints = LinkPoints(dict, i)
        # Should i delete linked points ???
        # A can only do this with making a lot of mistakes:
        if linkedPoints != []:
            dict[i] = linkedPoints # Use CSV or Dictianary ???
        i+=1
    print("Output csv file (As Dictianary - only for now) is : {0}".format(dict))
