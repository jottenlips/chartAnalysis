import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline
import os
import plotly
from plotly.graph_objs import Scatter, Layout
import numpy as np
import json


def getTeamWinsByIndex(index, json, numOfFiles):
    wins = []
    for i in range(numOfFiles):
        wins.append(json[i].Win[index])
    return wins

def getTeamLossesByIndex(index, json, numOfFiles):
    losses = []
    for i in range(numOfFiles):
        losses.append(json[i].Loss[index])
    return losses

fileNames = []
for file in os.listdir('cleanjson'):
    fileNames.append('/Users/johnottenlips/chartAnalysis/cleanjson/'+file)

# print(fileNames)


json = []
for i in range(30):
    json.append(pd.read_json(fileNames[i]))
teams = [] #list of all teams
dates = [] #list of all dates
print(json[1])
wins = []
for i in range(len(json)):
    if("Division" in json[0].Team[i]):
        continue
    else:
        teams.append(json[0]["Team"][i])
    wins.append(json[i].Win[1])
    dates.append(json[i]["Date Pulled"][1])
# print(Wins, dates)


print(getTeamWinsByIndex(4,json,30))
