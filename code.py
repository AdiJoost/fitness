import matplotlib.pyplot as plt
import csv

def main():
    activities = get_csv("csv_data/activity.csv")
    sleeps = get_csv("csv_data/sleep.csv")

def get_csv(file_name: str) -> list:
    with open(file_name, "r") as file:
        data = csv.reader(file):
    return_value = []
    for row in data:
        return_value.append(row)


if __name__ == "__main__":
    main();