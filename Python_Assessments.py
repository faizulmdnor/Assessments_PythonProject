import pandas as pd
import numpy as np

data = {
    'Name': ['Abdul Karim', 'Rizaruddin', 'Jamal', 'Suhaila', 'Jenifer Wong', 'Linda', 'Premala devi'],
    'Age': [55, 25, 28, 51, 26, 23, 35],
    'Height (cm)': [175, 169, 174, 160, 162, np.nan, 167],
    'Weight (kg)': [85, 75, 95, 58, 60, 67, np.nan]
}

# Q1 - Using pandas create dataframe and print
df = pd.DataFrame(data)
print(df)

# Q2 - replace NaN with 0
df_filled = df.fillna(0)
print('\nNew DataFrame after replacing NaN with 0:')
print(df_filled)

# Q3 - Modify the DataFrame to add a new column 'BMI' using the formula: weight (kg) / (height in m)^2. Handle rows with missing data appropriately (NaN).
print('\nRemove NaN data and add Height (m) and BMI:')
df.dropna(subset=['Height (cm)', 'Weight (kg)'], inplace=True)
df['Height (m)'] = df['Height (cm)']/100
df['BMI'] = df['Weight (kg)']/df['Height (m)']**2
print(df)