# import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord, Angle, Galactocentric
from astropy.io import ascii
from astropy.cosmology import WMAP9 as cosmo


def to_galacto(long, lat, redshift):
    distance = cosmo.comoving_distance(redshift)
    sc = SkyCoord(l=long * u.degree, b=lat * u.degree,
                  distance=distance, frame='galactic')
    gc = sc.transform_to(Galactocentric)
    return [gc.x.value, gc.y.value, gc.z.value]


# df = pd.read_csv('abell-galaxy-clusters-simplified.csv')
tbl = ascii.read('abell-galaxy-clusters-simplified.csv')

# Show galaxy distribution along Galactic Plane
long = Angle(tbl['GLON_2000'] * u.degree)
long = long.wrap_at(180 * u.degree)
lat = Angle(tbl['GLAT_2000'] * u.degree)

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='mollweide')
ax.scatter(long.radian, lat.radian, s=3, c='#b00020')
ax.set_xticklabels(['210°', '240°', '270°', '300°', '330°',
                    '0°', '30°', '60°', '90°', '120°', '150°'])
ax.grid(True)

plt.show()

# Show galaxy distribution in sphere, where GLONG is x-axis, GLAT is z-axis and Redshift is y-axis
# Will need math to transform coordinates from 3D to 2D
# Also perhaps transform coordinates?

data = pd.read_csv('../../data/abell-galaxy-clusters-simplified.csv')
rds = data[data['Redshift'].notna()]

cs = np.array([
    to_galacto(row.GLON_2000, row.GLAT_2000, row.Redshift)
    for row in rds.itertuples()
])

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(cs[:, 0], cs[:, 1], cs[:, 2], s=3, c='#b00020')
ax.set_xlabel('Mpc')
ax.set_ylabel('Mpc')
ax.set_zlabel('Mpc')
ax.grid(True)

plt.show()
