import numpy as np
import pandas as pd
import astropy.coordinates as coord
import astropy.units as u
import matplotlib.pyplot as plt
from math import pi, sqrt, atan2

def rad2deg(radians):
    return radians / pi * 180

def cart2sph(x, y, z):
    """
    Convert cartesian 3D coordinates to spherical coordinates.

    When returned, azimuth and elevation are expressed in radians.
    """
    x2plusy2 = x ** 2 + y ** 2
    radius = sqrt(x2plusy2 + z ** 2)
    elevation = atan2(z, sqrt(x2plusy2)) # theta
    azimuth = atan2(y, x)                # phi
    return (rad2deg(azimuth), rad2deg(elevation), radius)

data = pd.read_csv('./star-clusters.csv', index_col = 0)
filter = data['d'] < 10000

cs = np.array(
    [
        coord.SkyCoord(ra=row.RAhour * u.degree, dec=row.DEdeg * u.degree, distance = row.d * u.pc)
        for row in data[filter].itertuples()
    ]
)

# These are cartesian x,y,z coordinates
gcs = np.array([ c.transform_to(coord.Galactocentric) for c in cs ])

sphs = np.array([
    cart2sph(gc.x.value, gc.y.value, gc.z.value)
    for gc in gcs
])

azs = sphs[:,0]
rds = sphs[:,2]

fig = plt.figure()
ax = fig.add_subplot(projection='polar')
ax.scatter(azs, rds, s=3, c='#FFCC33')
plt.show()
