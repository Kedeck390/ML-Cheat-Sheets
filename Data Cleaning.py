Data Cleaning:

# Drop duplicates
df = df.drop_duplicates()

# Drop all rows where feature value equals some value 
df = df[df.<feature> != <>]

# Drop columns from the dataset
df.drop([<>, <>], axis = 1, inplace=True)

# Display unique values of '<>' feature
df.<feature>.unique()

# Fill missing feature values with (0, 1, string, etc.)
df.<feature>.fillna(<Whatever>, inplace = True)

# Replacing name for another
df.replace(<name to be replaced>, <new name>, inplace=True)

# Replacing names for another
df.replace(<[name1, name2, ...]>, <new name>, inplace=True)

# Display number of missing values by feature (categorical)
df.select_dtypes(include=['object']).isnull().sum()

# Fill missing categorical values
for column in df.select_dtypes(include=['object']):
    df[column] = df[column].fillna('Missing')
