import numpy as np
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord, Angle, Galactocentric
import matplotlib.pyplot as plt


def to_galactic(ra, dec):
    sc = SkyCoord(ra=ra * u.hourangle, dec=dec*u.degree)
    return [sc.galactic.l.value, sc.galactic.b.value]


galaxy_data = pd.read_csv('../../data/abell-galaxy-clusters-simplified.csv')
cluster_data = pd.read_csv('../../data/star-clusters.csv')

gal_long = Angle(galaxy_data['GLON_2000'] * u.degree)
gal_long = gal_long.wrap_at(180 * u.degree)
gal_lat = Angle(galaxy_data['GLAT_2000'] * u.degree)

cs = np.array([
    to_galactic(row.RAhour, row.DEdeg)
    for row in cluster_data.itertuples()
])

star_long = Angle(cs[:, 0] * u.degree)
star_long = star_long.wrap_at(180 * u.degree)
star_lat = Angle(cs[:, 1] * u.degree)

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(projection='mollweide')
ax.set_title('Galaxy Clusters and Star Clusters')
line1 = ax.scatter(gal_long.radian, gal_lat.radian, s=5, c='#b00020')
line2 = ax.scatter(star_long.radian, star_lat.radian, s=3, c='#ed8b00')
ax.set_xticklabels(['210°', '240°', '270°', '300°', '330°',
                    '0°', '30°', '60°', '90°', '120°', '150°'])
ax.legend([line1, line2], ['Galaxy clusters', 'Star clusters'])
ax.grid(True)

plt.show()
