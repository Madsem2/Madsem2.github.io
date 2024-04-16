

from Data_preparation import *

pd.set_option('display.max_rows', None)
focus_factors = np.array(df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().head(10).index)


print(df.head())

print(df.info())


#%% Bar plot per year
per_year = df['YEAR'].value_counts().sort_index()

plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

# Create bar chart
plt.bar(per_year.index, per_year.values, color='skyblue')

plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Crashes per year')
plt.xticks(per_year.index)

plt.savefig('\Databehandling\Crashes_per_year.png', bbox_inches='tight')

plt.show()

# %%
