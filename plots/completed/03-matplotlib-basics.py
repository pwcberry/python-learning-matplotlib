# Python Dojo: Matplotlib
# https://matplotlib.org/stable/index.html
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

###############################################################
# 1. Basic Plot
###############################################################
# typical = pd.read_excel('../../data/Active-Customers-1Form.xlsx', sheet_name='Typical Week')
# busiest = pd.read_excel('../../data/Active-Customers-1Form.xlsx', sheet_name='Busiest Week')
data = pd.read_csv('../../data/abell-galaxy-clusters-simplified.csv')

data.info()

# We don't have all the redshift values
avail = data[data['Redshift'].notna()]

magnitudes = data[:, 'Mag_10'].values
redshifts = data[:, 'Redshift'].values
###############################################################
# 2. Axes
###############################################################
plt.plot(magnitudes, redshifts)

# Our style choices
plt.style.available

plt.style.use('classic')
plt.plot(magnitudes, redshifts)

###############################################################
# 3. Labels
###############################################################
