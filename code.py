import matplotlib.pyplot as plt
import csv
import pandas as pd

def main():
    activity = pd.read_csv("csv_data/cool_activity.csv")
    steps = activity[["Datum", "Schritte"]]

    steps.loc["Schritte"] = pd.to_numeric(steps["Schritte"])
    steps.loc["Datum"] = pd.to_datetime(steps["Datum"], dayfirst=True)
    steps.loc["Schritte"] = steps["Schritte"] / 1000

    sleeps = pd.read_csv("csv_data/cool_sleeps_singleton.csv")
    sleeps["Datum"] = pd.to_datetime(sleeps["Startzeit"], dayfirst=True).dt.date
    sleep_time = sleeps[["Datum", "Minuten geschlafen"]]
    sleep_time.loc["Minuten geschlafen"] = pd.to_numeric(sleep_time["Minuten geschlafen"])
    sleep_time.loc["Minuten geschlafen"] = sleep_time["Minuten geschlafen"] * 100
    
    

    my_data = pd.concat([steps, sleep_time], axis=1)
    

    #ax = steps.plot(x="Datum")
    #sleep_time.plot(x="Datum")
    my_data.plot()
    print(my_data)
    plt.show()
    

if __name__ == "__main__":
    main();