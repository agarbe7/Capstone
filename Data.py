import pandas as pd

data = pd.read_csv("Music_and_Mental_Health_Data.csv")

print(data.shape)

print(data.info())

print(data.describe().T)

anxietyData = data.groupby("Anxiety").mean().round(2)

print(anxietyData)
