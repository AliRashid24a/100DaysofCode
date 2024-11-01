import pandas as pd

data = pd.read_csv("Day 24\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
"""
## using group by
res_df = data.groupby('Primary Fur Color').size()
print(res_df)

## using value counts
res_df = data['Primary Fur Color'].value_counts()
print(res_df)
"""
# Brute force

grey_squirels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirels = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Color": ['Gray','Cinnamon','Black'],
    "Count": [grey_squirels,red_squirels,black_squirels]
}

res_df = pd.DataFrame(data_dict)
res_df.to_csv('G:\\Projects\\100DaysofCode\\Day 24\\Squirel Counts.csv')