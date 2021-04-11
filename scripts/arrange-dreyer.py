import pandas as pd

print("Loading source...")
data = pd.read_excel('./NI2017.xls', sheet_name='Tabelle1')
data = data.convert_dtypes(convert_string=True).rename(columns={'Unnamed: 0':'R'})

# Extract Messier Catalog
filter = data['ID1'].str.contains(r'^M \d+', regex=True)
messier = data[filter]

print("Extracting Messier catalog...")
temp = messier.copy(deep=True)
s = temp['ID1'].str.extract(r'^M (\d+)', expand=False)

# Now sort into ascending order by Messier number
temp['Messier'] = pd.to_numeric(s)
messier = temp.sort_values(by='Messier')

print("Extracting open clusters...")
filter = data['TYPE'].str.contains(r'^(?:I+\d|IV\d|V\d|VI+\d|EN\+OCL)', regex=True)
open_clusters = data[filter]  

print("Extracting globular clusters...")
# Note: IC 1257 is a globular cluster; ref: http://adsabs.harvard.edu/full/1997AJ....113..688H
filter = data['TYPE'].str.contains(r'^(?:I|II|III|IV|V|VI|VII|VIII|IX|X|GCL)', regex=True)
globular_clusters = data[filter]

print("Extracting nebulae...")
filter = data['TYPE'].str.contains(r'^(?:SNR|EN|PN|RN)', regex=True)
nebulae = data[filter]

print("Extracting galaxies...")
# These are the morphological types for each galaxy
filter = data['TYPE'].str.contains(r'^(?:E[?\d]?|C|E\+C|E\/SB0|E\/S0|E\-S0|SB?[\?0\-abcdm]{1,3}|Im|IBm|Irr|Ring\s[ABCD])(?:\/P)*$')
galaxies = data[filter]

print("Extracting other objects...")
filter = data['TYPE'].str.contains(r'^(?:\*|NF|GxyP)')
others = data[filter]

print('Writing to Excel Workbook...')
with pd.ExcelWriter('NGC-IC.xlsx') as writer:
    data.to_excel(writer, sheet_name='Source', index=False)
    messier.to_excel(writer, sheet_name='Messier', index=False)
    open_clusters.to_excel(writer, sheet_name='Open Clusters', index=False)
    globular_clusters.to_excel(writer, sheet_name='Globular Clusters', index=False)
    nebulae.to_excel(writer, sheet_name='Nebulae', index=False)
    galaxies.to_excel(writer, sheet_name='Galaxies', index=False)
    others.to_excel(writer, sheet_name='Other', index=False)

print('Done.')
