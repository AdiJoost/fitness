from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def getDay(dates):
    returnList = []
    for day in dates:
        returnList.append(day.weekday() <= 4)
    return returnList

dataSet = pd.read_csv("csv_data/thereCantBeOnlyTwo.csv")
dataSet["ActivityDay"] = pd.to_datetime(dataSet["ActivityDay"])
dataSet["dayOfWeek"] = getDay(dataSet["ActivityDay"])
steps = dataSet[["StepTotal", "dayOfWeek"]]
plt.scatter(dataSet.index, dataSet["StepTotal"], c=dataSet["dayOfWeek"])
plt.show()



total_steps = 0
total_steps_divisor = 0
weekend_steps = 0
weekend_steps_divisor = 0
weekday_steps = 0
weekday_steps_divisor = 0
for index, row in dataSet.iterrows():
    total_steps += int(row["StepTotal"])
    total_steps_divisor += 1
    if (row["dayOfWeek"]):
        weekday_steps += int(row["StepTotal"])
        weekday_steps_divisor += 1
    else:
        weekend_steps += int(row["StepTotal"])
        weekend_steps_divisor += 1

print(f"Weekday_avrg: {weekday_steps/weekday_steps_divisor}"\
    f"\nWeekend_avrg: {weekend_steps/weekend_steps_divisor}"\
        f"\nTotal_avrg: {total_steps/total_steps_divisor}")