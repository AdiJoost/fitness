from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def getDay(dates):
    returnList = []
    for day in dates:
        returnList.append(day.weekday())
    return returnList

def getMean(df, col="StepTotal"):
    print(df)

def getMedian(df, col="StepTotal"):
    pass

def getRMSE(df, prediction, col="StepTotal"):
    pass

def getMAE(df, prediction, col="StepTotal"):
    pass

df = pd.read_csv("seperated_on_weekdays/day0_Person.csv")
getMean(df)

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