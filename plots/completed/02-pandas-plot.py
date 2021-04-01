# Python Dojo: Pandas

import pandas as pd

###############################################################
# 1. Basic Plot
###############################################################

data = pd.read_csv('../../data/Melbourne_Annual.csv')

data.plot(x='Year', y='Rainfall')

data.plot(x='Year', y='Temperature')


data = pd.read_excel('../../data/Active-Customers-1Form.xlsx',
                     sheet_name='Typical Users')


###############################################################
# 2. Histogram
###############################################################

bom = pd.read_excel('../../data/BOM_VIC_20210323.xlsx', sheet_name='Melbourne')

# Remove 'Station' column
bom = bom.drop(['Station'], axis=1)

# Use all data up to 31 Dec 2021
data = bom[:-82]
