#coding: UTF-8
#!/bin/env python3
import pandas as pd
import csv

# data = pd.read_csv("~/Programming/HackMoscow/Data/inputs.csv")

data = csv.DictReader(open("/home/ristle/Programming/HackMoscow/Data/inputs.csv"))

for row in data:
    print(row)
