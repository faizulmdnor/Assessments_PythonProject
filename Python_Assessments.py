import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Data Preparation
data = {
    'Name': ['Abdul Karim', 'Rizaruddin', 'Jamal', 'Suhaila', 'Jenifer Wong', 'Linda', 'Premala devi'],
    'Age': [55, 25, 28, 51, 26, 23, 35],
    'Height (cm)': [175, 169, 174, 160, 162, np.nan, 167],
    'Weight (kg)': [85, 75, 95, 58, 60, 67, np.nan]
}

# Q1 - Using pandas create dataframe and print
# Points: 5 (Beginner)
df = pd.DataFrame(data)
print(f"Q1 - Dataframe:\n{df}")

# Q2 - Replace NaN with 0
# Points: 5 (Beginner)
df_filled = df.fillna(0)
print('\nQ2 - New DataFrame after replacing NaN with 0:')
print(df_filled)

# Q3 - Modify the DataFrame to add a new column 'BMI' using the formula: weight (kg) / (height in m)^2. Handle rows with missing data appropriately (NaN).
# Points: 12 (Intermediate)
print('\nQ3 - Remove NaN, add columns Height (m) and BMI:')
df.dropna(subset=['Height (cm)', 'Weight (kg)'], inplace=True)
df['Height (m)'] = df['Height (cm)']/100
df['BMI'] = df['Weight (kg)']/df['Height (m)']**2
print(df)

# Q4 - Load data from production_output.csv
# Points: 8 (Intermediate)
prod_data = pd.read_csv('production_output.csv')
print(f"\nQ4 - Load production data from csv:")
print(prod_data)

# Q5 - Total output per day (Group by date and sum output/input)
# Points: 15 (Intermediate)
df_prod_data_day = prod_data.groupby(by=['date'])[['output','input']].sum().reset_index()
df_prod_data_day.rename(columns={'output': 'Total_output', 'input': 'Total_input'}, inplace=True)
print(f"\nQ5 - Total output and input by day:\n{df_prod_data_day}")

# Q6 - Average output per hour (assuming 24 hours of operation per day)
# Points: 15 (Intermediate)
df_prod_data_day['Average output per hour'] = (df_prod_data_day['Total_output']/24).round(3)
print("\nQ6 - Average output per hour:")
print(df_prod_data_day.to_string(index=False))

# Q6 Add column yield percentage (Total output / Total input) * 100
# Points: 15 (Intermediate)
df_prod_data_day['Yield (%)'] = (df_prod_data_day['Total_output'] / df_prod_data_day['Total_input'] * 100).round(2)
print("\nAdd column yield percentage")
print(df_prod_data_day)

# Q7 - Plotting with multiple y-axes (Bar chart and Line plot)
# Points: 40 (Advanced)
# Step 2: Set up figure and axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar chart: Total Output
ax1.bar(df_prod_data_day['date'], df_prod_data_day['Total_output'], color='skyblue', label='Total Output')
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Output', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.set_xticklabels(df_prod_data_day['date'], rotation=90)

# Step 3: Add a secondary y-axis for Yield (%)
ax2 = ax1.twinx()
ax2.plot(df_prod_data_day['date'], df_prod_data_day['Yield (%)'], color='orange', marker='o', label='Yield (%)')
ax2.set_ylabel('Yield (%)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_ylim(70, 100)

# Title and layout
plt.title('Daily Total Output and Yield Percentage')
fig.tight_layout()

# Save before plt.show() (best practice)
plt.savefig('daily_output_chart.png', dpi=300)

# Show plot
plt.show()
