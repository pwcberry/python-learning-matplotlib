import datetime
import pandas as pd

# import numpy as np
# import matplotlib.pyplot as plt

source_df = pd.read_excel('../data/BOM_VIC_20210323.xlsx', sheet_name='Melbourne')
dts = [pd.to_datetime(datetime.datetime(r.Year, r.Month, r.Day)) for r in source_df.itertuples(index=False)]

data = pd.DataFrame(dict([('Date', dts), ('Rainfall', source_df['Rainfall']), ('Maximum', source_df['Maximum']), ('Minimum', source_df['Minimum'])]))

total_rainfall = data[['Rainfall']].groupby([data['Date'].dt.year, data['Date'].dt.month]).sum()

mean_temperature = data[['Maximum', 'Minimum']].groupby([data['Date'].dt.year, data['Date'].dt.month]).mean()

zero_rainfall = total_rainfall[total_rainfall['Rainfall'] < 5]

hot_months = mean_temperature[mean_temperature['Maximum'] >= 25]

max_temperature = data[['Date', 'Maximum']].groupby([data['Date'].dt.year, data['Date'].dt.month]).max()

# Long-term monthly mean temperature
monthly_mean_temp_longterm = data['Maximum'].groupby([data['Date'].dt.month]).mean()

# 40 years: 40 * 365.25
recent_data = data[['Date', 'Maximum']][-14692:-1]

# Recent monthly mean temperature
monthly_mean_temp_recent = recent_data['Maximum'].groupby([data['Date'].dt.month]).mean()

# Now do the same for rainfall (up to 31 Dec 2020)
df = source_df[['Year','Month','Rainfall']][:-82].groupby([source_df['Year'], source_df['Month']]).agg({'Year': 'first', 'Month': 'first', 'Rainfall': 'sum'})
monthly_mean_rainfall_total_longterm = df[['Month', 'Rainfall']].groupby([df['Month']]).agg({'Month':'first','Rainfall':'mean'})

# Recent (1 Jan 1980 to 31 Dec 2020)
df2 = source_df[['Year','Month', 'Rainfall']][-14692:-82].groupby([source_df['Year'], source_df['Month']]).agg({'Year':'first', 'Month':'first', 'Rainfall':'sum'})
monthly_mean_rainfall_total_recent = df2[['Month', 'Rainfall']].groupby([df['Month']]).agg({'Month':'first','Rainfall':'mean'})

total_annual_rainfall_longterm = source_df[['Year', 'Rainfall']][:-82].groupby([source_df['Year']]).agg({'Year':'first','Rainfall':'sum'})
total_annual_rainfall_recent = source_df[['Year', 'Rainfall']][-14692:-82].groupby([source_df['Year']]).agg({'Year':'first','Rainfall':'sum'})
