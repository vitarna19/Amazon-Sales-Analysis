import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

# Load the dataset
data = pd.read_csv("C:/python codes/Amozon Sales Data/Amazon Sales data.csv")

# Display the complete dataset
print("Displaying complete Dataset.\n")
print(data)

# Return a tuple representing the dimensionality of the dataset
print("\nReturn a tuple representing the dimensionality of the Dataset.\n")
print(data.shape)

# Display columns in the dataset
print("\nDisplaying columns in Dataset.\n")
print(data.columns)

# Return the number of rows times number of columns
print("\nReturn the number of rows times number of columns.\n")
print(data.size)

# Print a concise summary of the dataset
print("\nPrint a concise summary of a Dataset.\n")
print(data.info())

# Generate descriptive statistics
print("\nGenerate descriptive statistics.\n")
print(data.describe())

# Return an integer value representing the array dimensions
print("\nReturn an integer value representing the array dimensions.\n")
print(data.ndim)

# Detect missing values and return the sum of the values
print("\nDetect missing values and return the sum of the values.\n")
print(data.isnull().sum())

# Return unique values of Order Priority column in the given dataset
print("\nReturn unique values of Order Priority column in given dataset.\n")
print(data['Order Priority'].unique())

# Make a copy of the dataset
print("\nMake a copy of the dataset.\n")
data_copy = data.copy()
print(data_copy)

# Count for unique values
print("\nCount for unique values.\n")
print(data['Order Priority'].value_counts())

# Remove null values from dataset
print("\nRemoving null values from dataset.\n")
data_copy.dropna(subset=['Unit Price', 'Unit Cost', 'Order Priority'], inplace=True)
print(data_copy)

# Generate descriptive statistics for the copied dataset
print("\nGenerate descriptive statistics.\n")
print(data_copy.describe())

# Creating Year, Month, Quarter, Day Columns in dataset
print("Creating Year, Month, Quarter, Day Columns in dataset")
data['Order Date'] = pd.to_datetime(data_copy['Order Date'], errors='coerce')
data_copy['Order_Year'] = data['Order Date'].dt.year
data_copy['Order_Month'] = data['Order Date'].dt.month
data_copy['Order_Quarter'] = data['Order Date'].dt.quarter
data_copy['Order_Day'] = data['Order Date'].dt.day

print(data_copy)

# Save the modified dataframe back to a CSV file
data_copy.to_csv("C:/python codes/Amozon Sales Data/Amazon Sales data_modified.csv", index=False)

# Print a concise summary of the dataset
print("\nPrint a concise summary of a Dataset.\n")
print(data_copy.info())

#Creating Dataframe only with neccessary values
data_selcol = data_copy[['Units Sold', 'Unit Price',  'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit','Order_Year', 'Order_Month', 'Order_Quarter', 'Order_Day']]

print("printing a new dataframe with only selected columns")
print(data_selcol)

# Detect missing values and return the sum of the values
print("\nDetect missing values and return the sum of the values.\n")
print(data_selcol.isnull().sum())

#Checking the correaltion
plt.figure(figsize=(16,9))
sns.heatmap(data_selcol.corr(method='pearson'), annot=True, vmin=-1, vmax=1, cmap='YlGnBu')
plt.xticks(rotation=90)
plt.show()

print("OBSERVASTION")
print("1- Units sold highly cause effect on Total Revenue ,Total Cost and Total Profit and moderately related to Unit Price and Unit Cost ")
print("2- Units sold depends on Order Priority List and Country asking for its sales.")
print("3- All the other related observations displayed in tableau.")