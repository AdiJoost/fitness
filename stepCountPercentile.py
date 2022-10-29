import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


stepsInternet = pd.read_csv("csv_data/internetSet.csv")
stepsPerson = pd.read_csv("csv_data/cool_activity.csv")


meanStepsPerson = stepsPerson.Schritte.mean()
print("Internet set percentiles:")
percentile = stepsInternet["StepTotal"].quantile(np.linspace(.01, 1, 99, 0), interpolation="lower")
print(percentile)


print("\n")
percentileOfPerson = percentile.where(percentile < meanStepsPerson).last_valid_index()

# Anteil personen, die unter meanStepsLiegen (abgerundet)
print(f"Person is in the: {int(percentileOfPerson*100)}th percentile with {int(meanStepsPerson)} steps\n")

print(f"Mean steps person: {meanStepsPerson:#.2f} \n")
print(f"Mean Steps Internet: {stepsInternet.StepTotal.mean():#.2f}")
