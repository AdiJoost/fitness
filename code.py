import matplotlib.pyplot as plt
import csv

def main():
    _, activities = get_csv("csv_data/activity.csv")
    _, sleeps = get_csv("csv_data/sleep.csv")
    print(activities)
    print(sleeps)

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