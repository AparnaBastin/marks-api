import pandas as pd

# Symbols to match
symbols_to_sum = ['‹', '“', '„']

# Read each file with appropriate encoding
df1 = pd.read_csv("data1.csv", encoding='cp1252')
df2 = pd.read_csv("data2.csv", encoding='utf-8')
df3 = pd.read_csv("data3.txt", encoding='utf-16', sep='\t')  # tab-separated

# Combine all data into one DataFrame
combined = pd.concat([df1, df2, df3], ignore_index=True)

# Filter rows where 'symbol' matches one of the target symbols
filtered = combined[combined['symbol'].isin(symbols_to_sum)]

# Convert the 'value' column to numeric (if it's not already)
filtered['value'] = pd.to_numeric(filtered['value'], errors='coerce')

# Sum the values
total = filtered['value'].sum()

print("Total sum for ‹, “, „ symbols:", total)
