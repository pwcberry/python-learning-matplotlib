import numpy as np
import pandas as pd
import astropy.coordinates as coord
import astropy.units as u
import matplotlib.pyplot as plt

data = pd.read_csv('./star-clusters.csv', index_col = 0)
filter = data['d'] < 2000
subset = data[filter]

cs = np.array(
    [
        coord.SkyCoord(ra=row.RAhour * u.hourangle, dec=row.DEdeg * u.degree, distance = row.d * u.pc)
        for row in subset.itertuples()
    ]
)

# Plot clusters to galacto-centric coordinates
# These are cartesian x,y,z coordinates
gcs = np.array([ c.transform_to(coord.Galactocentric) for c in cs ])

# Transform them into spherical coordinates
sphs = np.array([
    [g.spherical.lon.value, g.spherical.lat.value, g.spherical.distance.value]
    for g in gcs
])

fig = plt.figure(figsize=(18,9))
ax1 = fig.add_subplot(1,2,1, projection='polar')
ax1.set_title('Galactocentric')
ax1.set_xlabel('longitude')
ax1.set_yticklabels(['','4Kpc','','8Kpc','',''])
ax1.scatter(sphs[:,0], sphs[:,2], s=3, c='#FFCC33')

# Plot galactic longitude with distance from our solar system
gxs = np.array([
    [c.galactic.l.value, c.galactic.b.value, c.distance.value]
    for c in cs
])

ax2 = fig.add_subplot(122, projection='polar')
ax2.set_title('Galactic coordinates')
ax2.set_xlabel('longitude')
ax2.set_yticklabels(['','','','1Kpc','','','','2Kpc','',''])
ax2.scatter(gxs[:,0], gxs[:,2], s=3, c='#109910')

plt.show()

# Something's not right with the galacto-centric plot
# As the positions hover around 8kpcs around the centre.
# Perhaps I'm not understanding the transformation correctly?
