import pandas as pd

dsOrigins = ["internet", "Person"]
oldName = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
newName = ["Mo","Tu", "We", "Th", "Fr", "Sa", "Su"]

for i in range(7):
    for origin in dsOrigins:
        filePath = f"seperated_on_weekdays/day{i}_{origin}.csv"
        df = pd.read_csv(filePath)

        df["dayOfWeek"] = df["dayOfWeek"].replace(oldName[0], newName[0])
        df["dayOfWeek"] = df["dayOfWeek"].replace(oldName[1], newName[1])
        df["dayOfWeek"] = df["dayOfWeek"].replace(oldName[2], newName[2])
        df["dayOfWeek"] = df["dayOfWeek"].replace(oldName[3], newName[3])
        df["dayOfWeek"] = df["dayOfWeek"].replace(oldName[4], newName[4])
        df["dayOfWeek"] = df["dayOfWeek"].replace(oldName[5], newName[5])
        df["dayOfWeek"] = df["dayOfWeek"].replace(oldName[6], newName[6])


        with open (filePath, "w") as file:
            file.write(df.to_csv())


metadataSets = ["internet","Ninternet","Nperson","Person"]

for ds in metadataSets:
    filePath = f"seperated_on_weekdays/{ds}MetaData.csv"
    df = pd.read_csv(filePath)
    df["Weekday"] = df["Weekday"].replace(oldName[0], newName[0])
    df["Weekday"] = df["Weekday"].replace(oldName[1], newName[1])
    df["Weekday"] = df["Weekday"].replace(oldName[2], newName[2])
    df["Weekday"] = df["Weekday"].replace(oldName[3], newName[3])
    df["Weekday"] = df["Weekday"].replace(oldName[4], newName[4])
    df["Weekday"] = df["Weekday"].replace(oldName[5], newName[5])
    df["Weekday"] = df["Weekday"].replace(oldName[6], newName[6])

    with open (filePath, "w") as file:
        file.write(df.to_csv())