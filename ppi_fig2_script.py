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

strains_sorted_by_ppi = pd.Categorical(medians.index,ordered=True)
df_wilt_sert = df_wiltshire[df_wiltshire['varname'] == 'GAD1_cont']
df_wilt_sert['strain'] = df_wilt_sert['strain'].astype("category", categories=medians.index, ordered=True)
df_wilt_sert_nonan = df_wilt_sert[~df_wilt_sert['strain'].isnull()]
df_wilt_sert_nonan.sort_values(by='strain',inplace=True)

plt.figure()
ax = df_wilt_sert_nonan.plot(x='strain',y='mean',yerr='sd',fmt='o',figsize=(10,5),rot=70)
num_xticks = len(df_wilt_sert_nonan['strain'])
plt.xticks(range(num_xticks),
          df_wilt_sert_nonan['strain'].values)
plt.xlim([-1,num_xticks])
plt.ylabel('[GAD1] in cortex')
plt.show()
