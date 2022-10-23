import pandas as pd
import matplotlib.pyplot as plt

dfs = []
for i in range(7):
    dfs.append(pd.read_csv(f"seperated_on_weekdays/day{i}_person.csv"))

dfPerson = pd.read_csv("seperated_on_weekdays/NPersonMetaData.csv")
dfInet = pd.read_csv("seperated_on_weekdays/NinternetMetaData.csv")

print(dfPerson)
ax = dfPerson.plot(x="Weekday", y="MeanSteps", label="Mean Steps Person")
dfInet.plot(ax=ax, x="Weekday", y="MeanSteps", label="Mean Steps Internet")
plt.show()

ax = dfPerson.plot(x="Weekday", y=["RMSE", "MAE"], label=["RMSE Person", "MAE Person"])
dfInet.plot(ax=ax, x="Weekday", y=["RMSE", "MAE"], label=["RMSE Internet", "MAE Internet"])
plt.show()

ax = dfPerson.plot(x="Weekday", y=["nRMSE", "nMAE"], label=["Normalized RMSE Person", "Normalized MAE Person"])
dfInet.plot(ax=ax, x="Weekday", y=["nRMSE", "nMAE"], label=["Normalized RMSE Internet", "Normalized MAE Internet"])
plt.show()