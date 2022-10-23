from datetime import datetime
from math import floor, sqrt
from logger import Logger
import pandas as pd
import matplotlib.pyplot as plt

def getDay(dates):
    returnList = []
    for day in dates:
        returnList.append(day.weekday())
    return returnList

def getMean(df, col="StepTotal"):
    return floor((df[col].sum() / df[col].count()))

def getMedian(df, col="StepTotal"):
    sorted = df.sort_values(by=col, ignore_index=True)
    middle_index = int(floor(sorted[col].count() / 2))
    return floor(sorted.at[middle_index, col])

def getRMSE(df, prediction, col="StepTotal"):
    sum_error = 0
    for _, row in df.iterrows():
        sum_error += (row[col] - prediction) ** 2
    return floor(sqrt(sum_error / df[col].count()))

def getMAE(df, prediction, col="StepTotal"):
    sum_error = 0
    for _, row in df.iterrows():
        sum_error += abs(row[col] - prediction)
    return floor(sum_error / df[col].count())

def getCoolNumbers (df, path, weekday, isInternet=0, col="StepTotal"):
    mean = getMean(df, col=col)
    median = getMedian(df, col=col)
    rmse = getRMSE(df, mean, col=col)
    mae = getMAE(df, mean, col = col)
    coolNumbers = (weekday, mean, median, rmse, mae, isInternet)
    Logger.log_csv(coolNumbers, path)

def evaluateCSV(weekday, path="coolNumbers", isInternet=False):
    if isInternet:
        myPath = f"seperated_on_weekdays/day{weekday}_internet.csv"
    else:
        myPath = f"seperated_on_weekdays/day{weekday}_Person.csv"
    df = pd.read_csv(myPath)
    getCoolNumbers(df, path, weekday, isInternet=isInternet)

for i in range(6):
    evaluateCSV(i, path="internetMetaData", isInternet=True)

for i in range(6):
    evaluateCSV(i, path="PersonMetaData", isInternet=False)



"""
df = pd.read_csv("csv_data/thereCantBeOnlyTwo.csv")
df["ActivityDay"] = pd.to_datetime(df["ActivityDay"])
df["dayOfWeek"] = getDay(df["ActivityDay"])
newDf = df[["ActivityDay", "StepTotal", "dayOfWeek"]]
for day in range(7):
    mayDay = newDf.loc[newDf["dayOfWeek"] == day]
    mayDay.to_csv(f"seperated_on_weekdays/day{day}_Person.csv")


dataSet = pd.read_csv("csv_data/internetSet.csv")
dataSet["ActivityDay"] = pd.to_datetime(dataSet["ActivityDay"])
dataSet["dayOfWeek"] = getDay(dataSet["ActivityDay"])
steps = dataSet[["StepTotal", "dayOfWeek"]]
dataSet = dataSet.sort_values(by=["dayOfWeek"])
dataSet.plot(kind="scatter", x=range(5), y=range(5))
plt.show()

print(dataSet.head(20))

sorted = [[],[],[],[],[],[],[]]
for index, row in dataSet.iterrows():
    sorted[row["dayOfWeek"]].append(row["StepTotal"])
    
results = []
for days in sorted:
    results.append(sum(days)/len(days))

print(results)"""