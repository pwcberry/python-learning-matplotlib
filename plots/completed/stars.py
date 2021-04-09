import numpy as np
import pandas as pd
from astropy.coordinates import Angle
import astropy.units as u
import matplotlib.pyplot as plt

print('Loading star data...')
data = pd.read_csv('./data/stars-849.csv', index_col=0).convert_dtypes()

print('Converting to galactic longitude and latitude...')
galactic = np.array([(x.GLON, x.GLAT) for x in data.itertuples()])

long = Angle(galactic[:, 0] * u.degree)
long = long.wrap_at(180 * u.degree)
lat = Angle(galactic[:, 1] * u.degree)

print('Plotting...')
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(projection='mollweide')
ax.scatter(long.radian, lat.radian, s=3, color=(0,0,0,0.1))
ax.set_xticklabels(['210°', '240°', '270°', '300°', '330°',
                    '0°', '30°', '60°', '90°', '120°', '150°'])
ax.grid(True)
plt.show()
