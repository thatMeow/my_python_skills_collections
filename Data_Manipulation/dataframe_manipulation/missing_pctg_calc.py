ecpi_na = (ecpi.isnull().sum() / len(ecpi)) * 100
ecpi_na = ecpi_na.drop(ecpi_na[ecpi_na == 0].index).sort_values(ascending=False)[:30]
missing_data = pd.DataFrame({'Missing Ratio' :ecpi_na})
missing_data.head(20)
