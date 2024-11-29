import codecademylib3
import pandas as pd
import numpy as np

# code goes here

diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())

print(diabetes_data.shape[1])

print(len(diabetes_data.columns))


print(diabetes_data.shape[0])

print(len(diabetes_data))

print(diabetes_data.isnull().sum())

print(diabetes_data.info())

print(diabetes_data.describe())


diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

print(diabetes_data.isnull().sum())

print(diabetes_data[diabetes_data.isnull().any(axis=1)])

print(diabetes_data.dtypes)

print(diabetes_data.info())

print(diabetes_data['Outcome'].unique())

# Replace 'O' with 0
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0)

# Convert the column to int64
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype('int64')


for column in diabetes_data.columns:
    print(f"Value counts for {column}:")
    print(diabetes_data[column].value_counts())

for column in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']:
    median_value = diabetes_data[column].median()
    diabetes_data[column].replace(0, median_value, inplace=True)
