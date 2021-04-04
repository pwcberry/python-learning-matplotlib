import numpy as np
import pandas as pd

source_columns = {
    'RAhour': (26, 35),
    'DEdeg': (35, 43),
    'radius': (73, 80),
    'd': (143,151)
}

columns = [c for c in iter(source_columns.keys())]

cluster_data = np.empty((0,4))

with open('../data/Milky_Way_Star_Clusters_2/catalog.dat') as source_dat:
    for row in source_dat:
        item = []

        for i, c in enumerate(columns):
            i1, i2 = source_columns[c]
            item.append(float(row[i1:i2].lstrip().rstrip()))

        cluster_data = np.append(cluster_data, [item], axis=0)

df = pd.DataFrame(data=cluster_data, columns = columns)

df.to_csv('../data/star-clusters.csv')
