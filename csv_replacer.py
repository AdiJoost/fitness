
with open ("csv_data/sleep.csv", "r") as file:
    myData = file.read()
with open("csv_data/cool_sleeps.csv", "w") as file:
    file.write(myData.replace("'", "")) 