import pandas as pd 

df=pd.read_csv('pokemon_data.csv')

print(df.head(5))

## Read Header
df.columns

## Read Each Column
print(df[['Name', 'Type 1', 'HP']])
## Read