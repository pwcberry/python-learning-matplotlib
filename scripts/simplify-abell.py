import csv
from astropy import units as au
from astropy.coordinates import SkyCoord

# Starting byte index is one less than specified in the README
# End byte represents the index needed for the slice (same value as README)
source_columns = {
    "ACO": (0, 5),
    # "RA_1950": (6, 13),
    # "Dec_1950": (14, 20),
    "BMType": (42, 49),
    "Count": (52, 55),
    "RA_2000": (86, 93),
    "Dec_2000": (94, 100),
    # "GLON_1950": (118, 124),
    # "GLAT_1950": (125, 131),
    "Redshift": (133, 138),
    "Richness": (140, 141),
    "D_class": (142, 143),
    "Mag_10": (144, 148)
}

columns = [c for c in iter(source_columns.keys())]
target_columns = columns + ['GLON_2000', 'GLAT_2000']

def process(source_dat, writer):
    for data in source_dat:
        row = {}

        for c in columns:
            i1, i2 = source_columns[c]
            row[c] = data[i1:i2].lstrip().rstrip()

        c = SkyCoord(row['RA_2000'], row['Dec_2000'], unit=(au.hourangle, au.deg))
        row['RA_2000'] = c.ra.degree
        row['Dec_2000'] = c.dec.degree
        row['GLON_2000'] = c.galactic.l.degree
        row['GLAT_2000'] = c.galactic.b.degree

        writer.writerow(row)


with open("abell-galaxy-clusters-simplified.csv", "w", newline='') as dest_csv:
    writer = csv.DictWriter(dest_csv, fieldnames=target_columns)
    writer.writeheader()

    print('Extracting "table3"...')
    with open("ACO/table3.dat") as source_dat:
        process(source_dat, writer)

    print('Extracting "table4"...')
    with open("ACO/table4.dat") as source_dat:
        process(source_dat, writer)
    
    print('Extracting "table5"...')
    with open("ACO/table5.dat") as source_dat:
        process(source_dat, writer)
