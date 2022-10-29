import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


stepsInternet = pd.read_csv("csv_data/internetSet.csv")
stepsPerson = pd.read_csv("csv_data/cool_activity.csv")


meanStepsPerson = stepsPerson.Schritte.mean()
print(f"Mean steps person: {meanStepsPerson} \n")
print("Internet set percentiles:")
percentile = stepsInternet["StepTotal"].quantile(np.linspace(.1, 1, 9, 0), interpolation="lower")
print(percentile)


print("\n")
percentileOfPerson = percentile.where(percentile > meanStepsPerson).first_valid_index()
print(f"Person is in the: {int(percentileOfPerson*100)}th percentile with {int(meanStepsPerson)} steps")