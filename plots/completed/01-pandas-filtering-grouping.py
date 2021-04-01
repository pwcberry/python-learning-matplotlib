# Python Dojo: Pandas
# Visit: https://pandas.pydata.org/docs/getting_started/index.html

import pandas as pd

bom = pd.read_csv('../../data/BOM_VIC_20210323.xlsx')

# Remove unused column
bom = bom.drop(['Station'], axis=1)

# Remove 2021 values for consistency
bom = bom[:-82]

###############################################################
# 1. Filtering
###############################################################

# To filter, specify a boolean expression using equality operators
# Or a combination of equality expressions with the conjunctions of OR / AND
# Or the unity expression NOT

temp_filter = bom['Maximum'] >= 45
rain_filter = bom['Rainfall'] > 2

result = bom[temp_filter & rain_filter]

###############################################################
# 2. Grouping
###############################################################

# Mean monthly temperature
mean_temperature = bom[['Year', 'Month', 'Maximum', 'Minimum']].groupby(
    [bom['Year'], bom['Month']]).mean()

# Total rainfall per month
# This is dodgy
total_rainfall = bom[['Year', 'Month', 'Rainfall']
                     ].groupby([bom['Year'], bom['Month']]).sum()

# Use `agg` method instead
total_rainfall = bom[['Year', 'Month', 'Rainfall']].groupby([bom['Year'], bom['Month']]).agg({
    'Year': 'first',
    'Month': 'first',
    'Rainfall': 'sum'
})

# Now gather the mean for each month
monthly_mean_rainfall_total_longterm = total_rainfall[['Month', 'Rainfall']].groupby(
    [total_rainfall['Month']]).agg({'Month': 'first', 'Rainfall': 'mean'})

# Mean monthly temperature for last 40 years
FORTY_YEARS_IN_DAYS = int(40 * 365.25)
FORTY_YEARS_IN_MONTHS = 40 * 12

bom_40 = bom[-FORTY_YEARS_IN_DAYS:]

mean_temp_recent = bom_40[['Year', 'Month', 'Maximum', 'Minimum']].groupby(
    [bom_40['Year'], bom_40['Month']]).mean()

total_rainfall_recent = bom_40[['Year', 'Month', 'Rainfall']].groupby([bom_40['Year'], bom_40['Month']]).agg({
    'Year': 'first',
    'Month': 'first',
    'Rainfall': 'sum'
})

monthly_mean_rainfall_total_recent = total_rainfall_recent[['Month', 'Rainfall']].groupby(
    [total_rainfall_recent['Month']]
).agg({'Month': 'first', 'Rainfall': 'mean'})

# Yearly mean temperature
mean_temperature_annual = bom[['Year', 'Maximum']
                              ].groupby([bom['Year']]).mean()

# Yearly total rainfall
total_rainfall_annual = bom[['Year', 'Rainfall']].groupby([bom['Year']]).sum()

# Mean rainfall total per year
total_rainfall_annual['Rainfall'].mean()
