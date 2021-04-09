# Iterating over large datasets and transforming that data into Python objects is
# time-intensive. This script is to reduce that processing time by
# providing galactic longitude and latitude in the data so that plot times are reduced.

import pandas as pd
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u

print('Loading...')
source = pd.read_csv('./data/stars.csv', index_col=0).convert_dtypes()

print('Filtering...')
output = source[source['Mag'] <= 8.49]

print('Transforming to AstroPy StarCoord...')
cs = np.array([
    SkyCoord(ra=item.RA * u.hourangle, dec=item.Dec * u.degree)
    for item in output.itertuples()
])

print('Adding galactic longitude and latitude...')
column_count = output.shape[1]
galactic = np.array([(c.galactic.l.value, c.galactic.b.value) for c in cs])
output.insert(
    loc=column_count,
    column='GLON',
    value=galactic[:, 0]
)
output.insert(
    loc=column_count + 1,
    column='GLAT',
    value=galactic[:, 1]
)

print('Saving output...')
output.to_csv('./data/stars-849.csv')
