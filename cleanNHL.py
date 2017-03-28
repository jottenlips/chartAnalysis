import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import os


filename = '/Users/johnottenlips/chartAnalysis/json/2017-02-23.nhlstandings.json'
#filename = 'C:\Users\username\pathToFile\fileName.json'
#filename = 'fileName.json'
data = pd.read_json(filename)

filename2 = '/Users/johnottenlips/chartAnalysis/json/2017-02-28.nhlstandings.json'
#filename = 'C:\Users\username\pathToFile\fileName.json'
#filename = 'fileName.json'
data2 = pd.read_json(filename2)


fileNames = []
for file in os.listdir('json'):
    fileNames.append('/Users/johnottenlips/chartAnalysis/json/'+file)
print(fileNames)

jsonData = []
count = 0;
for fileName in fileNames:
    json = pd.read_json(fileName)
    jsonData.append(json)
    count+=1;
print(jsonData[0].Win)
print(jsonData[1].Win)

print(count)

# realData = []
# for i in range(len(jsonData)):
#     for j in range(len(jsonData[i])):
# #         #print(jsonData[i].Win[j])
#         realData.append(jsonData[jsonData[i].Win[j] != "W"])
# print(realData)
