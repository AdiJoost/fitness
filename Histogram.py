from keyword import kwlist
from sys import _xoptions
import pandas as pd
import matplotlib.pyplot as plt

stepsInternet = pd.read_csv("csv_data/internetSet.csv")
stepsInternet.hist(column="StepTotal")
plt.title("Schritte Internet", )

plt.show()

stepsPerson = pd.read_csv("csv_data/cool_activity.csv")
stepsPerson.hist(column="Schritte")
plt.title("Schritte Person")

plt.show()


sleepPerson = pd.read_csv("csv_data/cool_sleeps_singleton.csv")
plt.figure() 
sleepPerson.plot.hist(alpha=0.5)

plt.show()