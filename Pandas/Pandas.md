# Pandas Basics

## 1. Importing Pandas
```python
import pandas as pd
```

## 2. Creating a DataFrame
```python
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
```

## 3. Reading Data
```python
df = pd.read_csv('data.csv')  # Reading a CSV file
print(df.head())  # Display first 5 rows
```

## 4. Writing Data
```python
df.to_csv('output.csv', index=False)  # Save DataFrame to CSV
```

## 5. Appending DataFrames
```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)
```

## 6. Filtering Data
```python
filtered_df = df[df['Age'] > 25]
print(filtered_df)
```

## 7. Descriptive Statistics
```python
print(df.describe())  # Summary statistics
```

## 8. Handling Missing Data
```python
df.fillna(0, inplace=True)  # Replace NaN with 0
df.dropna(inplace=True)  # Remove rows with NaN values
```

## 9. Grouping Data
```python
grouped_df = df.groupby('Category').sum()
print(grouped_df)
```

## 10. Merging DataFrames
```python
df_merged = pd.merge(df1, df2, on='A', how='inner')
print(df_merged)
```

## 11. Sorting Data
```python
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)
```

## 12. Renaming Columns
```python
df.rename(columns={'Name': 'Full Name', 'Age': 'Years'}, inplace=True)
print(df)
```

## 13. Selecting Specific Columns
```python
selected_columns = df[['Name', 'Age']]
print(selected_columns)
```

## 14. Applying Functions to Columns
```python
df['Age in 5 Years'] = df['Age'].apply(lambda x: x + 5)
print(df)
```

## 15. Resetting and Setting Index
```python
df.set_index('Name', inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)
```

## 16. Creating a New Column
```python
df['Salary'] = [50000, 60000, 70000]
print(df)
```

## 17. Dropping a Column
```python
df.drop(columns=['Salary'], inplace=True)
print(df)
```

## 18. Checking for Duplicates
```python
duplicates = df.duplicated()
print(duplicates)
df.drop_duplicates(inplace=True)
print(df)
```

## 19. Value Counts
```python
print(df['Age'].value_counts())
```

## 20. Pivot Table
```python
pivot_table = df.pivot_table(index='Category', values='Age', aggfunc='mean')
print(pivot_table)
```
