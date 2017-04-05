import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import json, requests


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
# print(fileNames)

jsonData = []
count = 0;
for fileName in fileNames:
    with open(fileName) as json_data:
        d = json.load(json_data)
        # print(d)
    jsonData.append(d)
    count+=1;
# print(jsonData[0][0]["Team"])


print(jsonData[0])
for i in range(len(jsonData)):
    for j in range(len(jsonData[i])):
        try:
            if "Division" in jsonData[i][j]["Team"]:
                division = jsonData[i][j]["Team"]
                jsonData[i][j]["division"] = "DeleteRow";
            else:
                jsonData[i][j]["division"] = division;
                print(jsonData[i][j])
        except:
                pass
for for i in range(len(jsonData)):



print(i," ", j)
print(len(fileNames))
for i in range(len(jsonData)):
    with open("/Users/johnottenlips/chartAnalysis/cleanjson/"+fileNames[i], 'w') as outfile:
        json.dump(response, outfile, sort_keys=True, indent=2)
        outfile.close()




# print(count)

# realData = []
# for i in range(len(jsonData)):
#     for j in range(len(jsonData[i])):
# #         #print(jsonData[i].Win[j])
#         realData.append(jsonData[jsonData[i].Win[j] != "W"])
# print(realData)
