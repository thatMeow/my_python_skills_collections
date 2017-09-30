# list the columns that contain null values

df.columns[df.isnull().any()].tolist()
