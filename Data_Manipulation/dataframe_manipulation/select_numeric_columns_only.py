
numeric_variables = list(df.dtypes[dtypes != 'object'].index)
df[numeric_variables]


