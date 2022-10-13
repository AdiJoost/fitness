import matplotlib.pyplot as plt
import csv
import pandas as pd

def main():
    activities_header, activities = get_csv("csv_data/activity.csv")
    sleeps_header, sleeps = get_csv("csv_data/sleep.csv")
    activity = pd.read_csv("csv_data/cool_activity.csv")
    steps = activity[["Datum", "Schritte"]]

    steps["Schritte"] = pd.to_numeric(steps["Schritte"])
    print(steps)
    





def print_csv(header: list, data: list):
    print(header)
    for row in data:
        print (f"{row}\n_______________")


def get_csv(file_name: str) -> list:
    with open(file_name, "r") as file:
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        header.append(header)
        data = []
        for row in csvreader:
            data.append(row)
    return header, data

if __name__ == "__main__":
    main();