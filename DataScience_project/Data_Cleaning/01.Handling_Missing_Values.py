import pandas as pd

# ================================================================
# 1. # Reading the dataset
# ================================================================

data = pd.read_csv('Unclear_dataset.csv')
print(data)

# Inspecting first few rows of the dataset
print("\n\nFirst few rows of the dataset:")
print(data.head())

# ================================================================
# 2. Info about the dataset
# ================================================================

print("\n\nInfo about the dataset:")
print(data.info())

# ================================================================
# 3. Identifying missing values
# ================================================================

print("\n\nMissing values in each column:")
print(data.isnull().sum())

# ================================================================
# 4. Handliing data types
# ================================================================

data['Age'] = data['Age'].replace(['Twenty One','Eighteen'], [21, 18])
data['Marks'] = data['Marks'].replace('Absent',0)

print("\n\nData types of each column:")
print(data.dtypes)   
               
# Converting 'age' and 'marks' columns to numeric
data['Age'] = data['Age'].astype(int)
data['Marks'] = data['Marks'].astype(float)
print("\n\nData types after conversion:")
print(data.dtypes)


# ================================================================
# 5. Handling missing values
# ================================================================

# Option 1: Dropping rows with missing values
data_dropped = data.dropna()
print("\n\nDataset after dropping rows with missing values:")
print(data_dropped)

# Option 2: Filling missing values with mean
data = data.fillna(data.mean(numeric_only=True))
print("\n\nDataset after filling missing values with mean:")
print(data)

# ================================================================
# 6. impute missing values with median
# ================================================================

data = data.fillna(data.median(numeric_only=True))
print("\n\nDataset after filling missing values with median:")
print(data)

# ================================================================
# 7. Handling Duplicate Values
# ================================================================

# Checking for duplicate rows
print("\n\nDuplicate rows in the dataset:")
print(data.duplicated().sum())

# Removing duplicate rows
data = data.drop_duplicates()
print("\n\nDataset after removing duplicate rows:")
print(data)

# Resetting index after dropping duplicates
data = data.reset_index(drop=True)
print("\n\nDataset after resetting index:")
print(data)

# ================================================================
# 8. Standardizing column names
# ================================================================

# Standardizing column names to lowercase
print("\n\nDataset before standardizing column names:")
print(data.columns)

data.columns = data.columns.str.lower()
print("\n\nDataset after standardizing column names:")
print(data.columns)

# ================================================================
# 9. Output a cleaned dataset and brief cleaning log
# ================================================================

# Saving the cleaned dataset to a new CSV file
data.to_csv('Cleaned_dataset.csv', index=False)
print("\n\nCleaned dataset saved as 'Cleaned_dataset.csv'.")

# Cleaning log
print("\n\nCleaning Log:")
print("1. Replaced non-numeric values in 'Age' and 'Marks' columns with numeric values.")
print("2. Converted 'Age' and 'Marks' columns to appropriate data types.")
print("3. Handled missing values by filling them with mean and median.")
print("4. Removed duplicate rows and reset index.")