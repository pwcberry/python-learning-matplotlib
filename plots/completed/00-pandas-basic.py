# Python Dojo: Pandas
# Visit: https://pandas.pydata.org/docs/getting_started/index.html

import pandas as pd

# Loading a file

###############################################################
# 1. Load from CSV
###############################################################

bom = pd.read_csv('../../data/Melbourne_Annual.csv')

###############################################################
# 2. Inspect a DataFrame
###############################################################

# Print a concise summary
bom.info()

# Show the number of elements
bom.size

# Show the shape of the data frame
bom.shape

# Show the first 5 rows (default)
bom.head()

# Show the first 10 rows
bom.head(10)

# Show the last 5 rows (default)
bom.tail()

# Show the last 10 rows
bom.tail(10)

# Show missing values in the data frame (returns Booleans, and can be used in filtering)
bom.isna()

# Show a range
bom[0:6]


###############################################################
# 3. Inspect a Series
###############################################################

# Load Excel workbook
bom = pd.read_excel('../../data/BOM_VIC_20210323.xlsx')

rainfall = bom['Rainfall']

# Show missing values
rainfall.isna()

# Fill missing values (returns new Series)
rainfall = rainfall.fillna(0.0)

# Show counts for each value
rainfall.value_counts()

# Show maximum
rainfall.max()

# Show minimum
rainfall.min()

# Show mean
rainfall.mean()

# Demonstrate how many days in current year
years = bom['Year']
years.value_counts()

###############################################################
# 4. Use with numpy
###############################################################
