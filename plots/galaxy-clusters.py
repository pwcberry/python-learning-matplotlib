# import pandas as pd
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord, Angle
from astropy.io import ascii

# df = pd.read_csv('abell-galaxy-clusters-simplified.csv')
tbl = ascii.read('abell-galaxy-clusters-simplified.csv')

# Show galaxy distribution along Galactic Plane
long = Angle(tbl['GLON_2000'] * u.degree)
long = long.wrap_at(180 * u.degree)
lat = Angle(tbl['GLAT_2000'] * u.degree)

fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(111, projection = 'mollweide')
ax.scatter(long.radian, lat.radian)
ax.set_xticklabels(['210','240','270','300','330','0','30','60','90','120','150'])
ax.grid(True)

plt.show()

# Show galaxy distribution in sphere, where GLONG is x-axis, GLAT is z-axis and Redshift is y-axis
# Will need math to transform coordinates from 3D to 2D
# Also perhaps transform coordinates?

