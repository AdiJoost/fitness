import matplotlib.pyplot as plt
import csv
import pandas as pd

def main():
    activity = pd.read_csv("csv_data/cool_activity.csv")
    steps = activity[["Datum", "Schritte"]]

    steps["Schritte"] = pd.to_numeric(steps["Schritte"])
    steps["Datum"] = pd.to_datetime(steps["Datum"], dayfirst=True)
    steps.plot(x="Datum")
    plt.show()
    

if __name__ == "__main__":
    main();