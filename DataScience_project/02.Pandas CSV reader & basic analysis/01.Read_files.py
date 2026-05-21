import pandas as pd

# ===============================================================
# Reading CSV file into a DataFrame
# ===============================================================

read_csv = pd.read_csv('students.csv')
print("CSV file data is: ")
print(read_csv)

# Inspecting first few rows of the DataFrame
print("\n\nFirst 5 rows of the DataFrame: ")
print(read_csv.head())

# Inspecting last few rows of the DataFrame
print("\n\nLast 5 rows of the DataFrame: ")
print(read_csv.tail())

# ===============================================================
# Reading Excel file into a DataFrame
# ===============================================================

read_excel = pd.read_excel('students_dataset.xlsx')
print("\n\nExcel file data is: ")
print(read_excel)

# Inspecting first few rows of the DataFrame
print("\n\nFirst 5 rows of the DataFrame: ")
print(read_excel.head())

# Inspecting last few rows of the DataFrame
print("\n\nLast 5 rows of the DataFrame: ")
print(read_excel.tail())

# ===============================================================
# Compute summary stats(mean, median, mode) for the 'Age' column
# ===============================================================

print("\n\nSummary statistics for the 'Age' column: ")
print(read_excel.describe(include = 'all'))

#==============================================================
# Filtering data and saving it to Excel file
#==============================================================

# Filter Rows where Attendance is greater than 85
filtered_data = read_excel[read_excel['Attendance'] > 85]
print("\n\nFiltered data where Attendance is greater than 85: ")
print(filtered_data)

# Grouping data by 'Name' and Sum of all marks
grouped_data = read_excel.groupby('Name')[['Math', 'Science', 'English']].sum()
print("\n\nGrouped data by 'Name' and Sum of all marks: ")
print(grouped_data)

# Selecting data
selected_data = read_excel[['Math', 'Science','English']]  # Selecting specific columns
print("\n\nSelected columns (Math, Science, and English): ")
print(selected_data)

#=================================================================
# Slicing data and creating new columns
#=================================================================

# Slicing data
sliced_data = read_excel[1:4]  # Selecting rows from index 1 to 3
print("\n\nSliced data (rows from index 1 to 3): ")
print(sliced_data)

# Slicing using loc 
loc_sliced_data = read_excel.loc[1:3]  # Using loc to slice
print("\n\nSliced data using loc (rows from index 1 to 3): ")
print(loc_sliced_data)

# Slicing using iloc
iloc_sliced_data = read_excel.iloc[1:4]  # Using iloc to slice
print("\n\nSliced data using iloc (rows from index 1 to 3): ")
print(iloc_sliced_data)

# Creating a new column 'Total' by summing up 'Math', 'Science', and 'English' columns
read_excel['Total'] = read_excel['Math'] + read_excel['Science'] + read_excel['English']
print("\n\nDataFrame with new 'Total' column: ")
print(read_excel)

# Creating a new column 'Percentage' by calculating the percentage of total marks
read_excel['Percentage'] = (read_excel['Total'] / 300) * 100
print("\n\nDataFrame with new 'Percentage' column: ")
print(round(read_excel, 2))  
