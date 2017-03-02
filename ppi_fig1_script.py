import pandas as pd
import matplotlib.pyplot as plt

df_willott = pd.read_csv('Willott1_table-1.csv',skiprows=6,header=0) # df is short for 'dataframe'
df_wiltshire = pd.read_csv('Wiltshire3_means.csv',skiprows=5,header=0)
wiltshire_strains = df_wiltshire['strain'].unique()
inds_of_strains_in_both = df_willott['strain'].isin(wiltshire_strains)
df_willott = df_willott[inds_of_strains_in_both]
grouped = df_willott.groupby(['strain'])
df_ppi_tot = pd.DataFrame({col:vals['PPI_tot'] for col,vals in grouped})
medians = df_ppi_tot.median().sort_values()
df_ppi_tot = df_ppi_tot[medians.index]
# use the columns in the dataframe, ordered sorted by median value
# return axes so changes can be made outside the function
plt.figure(figsize=(10,5))
plt.xlabel('Mouse strain')
plt.ylabel('PPI')
df_ppi_tot.boxplot(rot=45, figsize=(10,5),return_type='axes')
plt.show()
