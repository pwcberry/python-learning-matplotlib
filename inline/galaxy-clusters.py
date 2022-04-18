import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from astropy import units as u 
from astropy.coordinates import SkyCoord, Angle, Galactocentric
from astropy.cosmology import WMAP9 as cosmo
from colors import colors

# A convenience function to transform the data so it can be plotted easier
def to_galacto_centric(long, lat, redshift):
    distance = cosmo.comoving_distance(redshift)
    sc = SkyCoord(l=long * u.degree, b=lat * u.degree,
                  distance=distance, frame='galactic')
    gc = sc.transform_to(Galactocentric)
    return [gc.x.value, gc.y.value, gc.z.value]

galaxy_clusters = pd.read_csv('../data/abell-galaxy-clusters-simplified.csv')

rds = galaxy_clusters[galaxy_clusters['Redshift'].notna()]

cs = np.array([
    to_galacto_centric(row.GLON_2000, row.GLAT_2000, row.Redshift)
    for row in rds.itertuples()
])

# This will pop-up an interactive window that you should be able to pan
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
ax.scatter(cs[:, 0], cs[:, 1], cs[:, 2], s=3, c=colors['red'])
ax.set_xlabel('Mpc')
ax.set_ylabel('Mpc')
ax.set_zlabel('Mpc')
ax.grid(True);

plt.show()

