# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def perfq(initial, final):
    return (final - initial) / (final + initial)


# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("/home/peo/Downloads/tt_respt.csv")

print(len(data.columns))
print(data.info())
print(data.describe())
print(data.describe().transpose())

print(data.describe().transpose()[1:3])
print(data[::-1]) #reverse the data frame
print(data['Kibana-initial'])
print(data[['Kibana-initial', 'QN-initial']]) #create a list of header keyword between []

print(data.head())
#column renaming
data.columns = ['Scenario', 'KibanaInitial', 'KibanaClone', 'KibanaMove', 'QNInitial', 'QNClone', 'QNMove']

print('Show a column\n', data.KibanaInitial) # direct access to a column

print('Multiply two columns\n', data.KibanaInitial * data.QNInitial) # multiply two columns

data['NewColumn'] = data.KibanaInitial * data.QNInitial #Add a new column

# Remove a column and return a new obj, `1` means column axis, while `0` (default) is the row axis
print('Remove a column\n', data.drop('NewColumn', 1))

filter = data.KibanaInitial > 28

print(filter)

# Filter the dataset with row where filter is true
print('Single filtered dataframe\n', data[filter])

filter2 = data.QNInitial > 70

# Double filtering bitwise logical operator
print('Double filtered dataframe\n', data[filter & filter2])
print('Unique values in QNInitial\n', data.QNInitial.unique()) # Show unique values of a column

# Uses integer to access an element
print('Element iat\n', data.iat[0,2])
# Uses labels to access an element
print('Element at\n', data.at[0,'KibanaInitial'])

print(data.head())
vis1 = sns.distplot(data['KibanaInitial'])
plt.show()
