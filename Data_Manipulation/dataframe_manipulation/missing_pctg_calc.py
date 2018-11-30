ecpi_na = (ecpi.isnull().sum() / len(ecpi)) * 100
ecpi_na = ecpi_na.drop(ecpi_na[ecpi_na == 0].index).sort_values(ascending=False)[:30]
missing_data = pd.DataFrame({'Missing Ratio' :ecpi_na})
missing_data.head(20)

#2
#missing data
total = df_train.isnull().sum().sort_values(ascending=False)
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)
