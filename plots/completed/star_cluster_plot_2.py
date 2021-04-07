import numpy as np
import pandas as pd
import astropy.coordinates as coord
import astropy.units as u
import matplotlib.pyplot as plt

data = pd.read_csv('./star-clusters.csv', index_col=0)

cs = np.array(
    [
        coord.SkyCoord(ra=row.RAhour * u.hourangle,
                       dec=row.DEdeg * u.degree, distance=row.d * u.pc)
        for row in data.itertuples()
    ]
)

long = coord.Angle([c.galactic.l.value * u.degree for c in cs])
long = long.wrap_at(180 * u.degree)
lat = coord.Angle([c.galactic.b.value * u.degree for c in cs])

fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, projection='mollweide')
ax.scatter(long.radian, lat.radian, s=3, c='orange')
ax.set_xticklabels(['210°', '240°', '270°', '300°', '330°',
                    '0°', '30°', '60°', '90°', '120°', '150°'])
ax.grid(True)
plt.show()
